#!/usr/bin/env python3
"""Validate a deck-video research run's evidence artifacts.

Usage:
    python scripts/validate_evidence.py RUN_DIR
    python scripts/validate_evidence.py --selftest

Parses source_registry.md and evidence_matrix.md (pipe tables) inside
RUN_DIR and checks IDs, references, enums, locators, and lineage, plus a
set of best-practice warnings. Every finding is printed as one line:
    ERROR <CODE>: <detail>
    WARN <CODE>: <detail>

Exit codes:
    0 - no errors (warnings allowed)
    1 - at least one error
    2 - usage or IO error (RUN_DIR missing entirely, unreadable files)
"""

import argparse
import glob
import json
import os
import re
import shutil
import sys
import tempfile

REGISTRY_HEADER = (
    "| ID | Title | Org/Author | URL | Pub date | Accessed | Type | Primary "
    "| Independent | Pass | Status | Topics | Caveats | Lineage | Score |"
)
MATRIX_HEADER = (
    "| Claim ID | Claim | Class | Supports | Contradicts | Locator | Metric "
    "| Confidence | Caveats | Disposition |"
)

REGISTRY_COLS = [
    "ID", "Title", "Org/Author", "URL", "Pub date", "Accessed", "Type",
    "Primary", "Independent", "Pass", "Status", "Topics", "Caveats",
    "Lineage", "Score",
]
MATRIX_COLS = [
    "Claim ID", "Claim", "Class", "Supports", "Contradicts", "Locator",
    "Metric", "Confidence", "Caveats", "Disposition",
]

SOURCE_ID_RE = re.compile(r"^S\d{2,}$")
CLAIM_ID_RE = re.compile(r"^C\d{2,}$")

STATUS_ENUM = {"imported", "downloaded", "omitted", "inaccessible"}
PRIMARY_ENUM = {"primary", "secondary"}
INDEPENDENT_ENUM = {"independent", "interested"}
CLASS_ENUM = {"observed", "interpretation", "forecast", "inference"}
CONFIDENCE_ENUM = {"strong", "moderate", "weak", "speculative"}
DISPOSITION_ENUM = {"include", "qualify", "omit", "investigate"}


class Finding:
    def __init__(self, severity, code, detail):
        self.severity = severity
        self.code = code
        self.detail = detail

    def line(self):
        return "%s %s: %s" % (self.severity, self.code, self.detail)


def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def parse_table(path, expected_header, findings, label):
    """Parse a pipe table. Returns list of (line_no, cells) or None on schema
    failure (an E_SCHEMA finding has already been appended)."""
    if not os.path.isfile(path):
        findings.append(Finding("ERROR", "E_SCHEMA",
                                 "%s: missing table file" % path))
        return None
    try:
        text = read_text(path)
    except (OSError, UnicodeDecodeError) as e:
        findings.append(Finding("ERROR", "E_SCHEMA",
                                 "%s: unreadable/unparseable (%s)" % (path, e)))
        return None

    lines = text.splitlines()
    header_idx = None
    for i, raw in enumerate(lines):
        s = raw.strip()
        if s.startswith("|"):
            header_idx = i
            break
    if header_idx is None:
        findings.append(Finding("ERROR", "E_SCHEMA",
                                 "%s: no pipe table found" % path))
        return None

    header_line = lines[header_idx].strip()
    if header_line != expected_header:
        findings.append(Finding(
            "ERROR", "E_SCHEMA",
            "%s: %s header row does not match expected schema" % (path, label)))
        return None

    rows = []
    i = header_idx + 2  # skip header + separator line
    n_cols = len(REGISTRY_COLS) if label == "registry" else len(MATRIX_COLS)
    while i < len(lines):
        s = lines[i].strip()
        if not s.startswith("|"):
            break
        inner = s
        if inner.startswith("|"):
            inner = inner[1:]
        if inner.endswith("|"):
            inner = inner[:-1]
        cells = [c.strip() for c in inner.split("|")]
        if len(cells) != n_cols:
            findings.append(Finding(
                "ERROR", "E_SCHEMA",
                "%s: row %d has %d cells, expected %d"
                % (path, i + 1, len(cells), n_cols)))
        else:
            rows.append((i + 1, cells))
        i += 1
    return rows


def split_ids(cell):
    """Split a comma-separated ID cell; '-' or empty means no entries."""
    cell = cell.strip()
    if cell == "" or cell == "-":
        return []
    return [tok.strip() for tok in cell.split(",") if tok.strip()]


def check_registry(rows, findings):
    """Returns (registry_ids set, rows_by_id dict of id -> cells)."""
    registry_ids = set()
    rows_by_id = {}
    seen = set()
    for line_no, cells in rows:
        rid = cells[0]
        primary = cells[7]
        independent = cells[8]
        status = cells[10]
        lineage = cells[13]
        score = cells[14]

        registry_ids.add(rid)
        rows_by_id[rid] = cells

        if not SOURCE_ID_RE.match(rid):
            findings.append(Finding(
                "ERROR", "E_ID",
                "source_registry.md row %d: invalid source ID '%s'"
                % (line_no, rid)))
        if rid in seen:
            findings.append(Finding(
                "ERROR", "E_ID",
                "source_registry.md row %d: duplicate source ID '%s'"
                % (line_no, rid)))
        seen.add(rid)

        if status not in STATUS_ENUM:
            findings.append(Finding(
                "ERROR", "E_ENUM",
                "source_registry.md row %d (%s): invalid Status '%s'"
                % (line_no, rid, status)))
        if primary not in PRIMARY_ENUM:
            findings.append(Finding(
                "ERROR", "E_ENUM",
                "source_registry.md row %d (%s): invalid Primary '%s'"
                % (line_no, rid, primary)))
        if independent not in INDEPENDENT_ENUM:
            findings.append(Finding(
                "ERROR", "E_ENUM",
                "source_registry.md row %d (%s): invalid Independent '%s'"
                % (line_no, rid, independent)))
        if score != "-":
            valid_score = False
            try:
                sv = int(score)
                valid_score = 0 <= sv <= 10
            except ValueError:
                valid_score = False
            if not valid_score:
                findings.append(Finding(
                    "ERROR", "E_ENUM",
                    "source_registry.md row %d (%s): invalid Score '%s'"
                    % (line_no, rid, score)))

    # lineage references (second pass, needs full registry_ids)
    for line_no, cells in rows:
        rid = cells[0]
        lineage = cells[13]
        for tok in split_ids(lineage):
            if tok not in registry_ids:
                findings.append(Finding(
                    "ERROR", "E_LINEAGE",
                    "source_registry.md row %d (%s): Lineage references "
                    "unknown source ID '%s'" % (line_no, rid, tok)))
        if lineage != "-" and lineage != "":
            # sanity: bare '-' or comma list already handled by split_ids;
            # nothing else to validate for format per spec.
            pass

    return registry_ids, rows_by_id


def check_matrix(rows, registry_ids, findings):
    claim_rows = []
    seen = set()
    for line_no, cells in rows:
        cid = cells[0]
        cls = cells[2]
        supports = cells[3]
        contradicts = cells[4]
        locator = cells[5]
        confidence = cells[7]
        caveats = cells[8]
        disposition = cells[9]

        if not CLAIM_ID_RE.match(cid):
            findings.append(Finding(
                "ERROR", "E_ID",
                "evidence_matrix.md row %d: invalid claim ID '%s'"
                % (line_no, cid)))
        if cid in seen:
            findings.append(Finding(
                "ERROR", "E_ID",
                "evidence_matrix.md row %d: duplicate claim ID '%s'"
                % (line_no, cid)))
        seen.add(cid)

        if cls not in CLASS_ENUM:
            findings.append(Finding(
                "ERROR", "E_ENUM",
                "evidence_matrix.md row %d (%s): invalid Class '%s'"
                % (line_no, cid, cls)))
        if confidence not in CONFIDENCE_ENUM:
            findings.append(Finding(
                "ERROR", "E_ENUM",
                "evidence_matrix.md row %d (%s): invalid Confidence '%s'"
                % (line_no, cid, confidence)))
        if disposition not in DISPOSITION_ENUM:
            findings.append(Finding(
                "ERROR", "E_ENUM",
                "evidence_matrix.md row %d (%s): invalid Disposition '%s'"
                % (line_no, cid, disposition)))

        supports_ids = split_ids(supports)
        contradicts_ids = split_ids(contradicts)
        for tok in supports_ids:
            if tok not in registry_ids:
                findings.append(Finding(
                    "ERROR", "E_REF",
                    "evidence_matrix.md row %d (%s): Supports references "
                    "unknown source ID '%s'" % (line_no, cid, tok)))
        for tok in contradicts_ids:
            if tok not in registry_ids:
                findings.append(Finding(
                    "ERROR", "E_REF",
                    "evidence_matrix.md row %d (%s): Contradicts references "
                    "unknown source ID '%s'" % (line_no, cid, tok)))

        if disposition in ("include", "qualify") and (locator == "-" or locator == ""):
            findings.append(Finding(
                "ERROR", "E_LOCATOR",
                "evidence_matrix.md row %d (%s): Disposition '%s' requires "
                "a Locator" % (line_no, cid, disposition)))

        claim_rows.append({
            "line_no": line_no, "id": cid, "class": cls,
            "supports": supports_ids, "contradicts": contradicts_ids,
            "locator": locator, "confidence": confidence,
            "caveats": caveats, "disposition": disposition,
        })
    return claim_rows


def check_forecast_warn(claim_rows, findings):
    for c in claim_rows:
        if (c["disposition"] == "include" and c["class"] == "forecast"
                and c["confidence"] == "strong"):
            findings.append(Finding(
                "WARN", "W_FORECAST",
                "evidence_matrix.md row %d (%s): included forecast claim "
                "with strong confidence" % (c["line_no"], c["id"])))


def check_concentration_warn(claim_rows, findings):
    included = [c for c in claim_rows if c["disposition"] in ("include", "qualify")]
    total = len(included)
    if total < 2:
        return
    counts = {}
    for c in included:
        for sid in set(c["supports"]):
            counts[sid] = counts.get(sid, 0) + 1
    for sid, cnt in sorted(counts.items()):
        if cnt / total > 0.5:
            findings.append(Finding(
                "WARN", "W_CONCENTRATION",
                "source '%s' supports %d/%d (>50%%) of include/qualify claims"
                % (sid, cnt, total)))


def lineage_chain(sid, rows_by_id, visited=None):
    if visited is None:
        visited = set()
    result = set()
    for tok in split_ids(rows_by_id.get(sid, [""] * 15)[13]) if sid in rows_by_id else []:
        if tok in visited:
            continue
        visited.add(tok)
        result.add(tok)
        result |= lineage_chain(tok, rows_by_id, visited)
    return result


def check_circular_warn(claim_rows, rows_by_id, findings):
    for c in claim_rows:
        sup = list(dict.fromkeys(c["supports"]))
        if len(sup) < 2:
            continue
        flagged = False
        for a in sup:
            chain = lineage_chain(a, rows_by_id)
            for b in sup:
                if b == a:
                    continue
                if b in chain:
                    findings.append(Finding(
                        "WARN", "W_CIRCULAR",
                        "evidence_matrix.md row %d (%s): Supports source "
                        "'%s' lineage chain contains sibling support '%s'"
                        % (c["line_no"], c["id"], a, b)))
                    flagged = True
                    break
            if flagged:
                break


def parse_date(s):
    import datetime
    try:
        return datetime.datetime.strptime(s.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None


def check_stale_warn(registry_rows, run_dir, findings):
    manifest_path = os.path.join(run_dir, "run_manifest.json")
    if not os.path.isfile(manifest_path):
        return
    try:
        manifest = json.loads(read_text(manifest_path))
    except (OSError, UnicodeDecodeError, ValueError):
        return
    as_of = manifest.get("as_of_date") if isinstance(manifest, dict) else None
    if not as_of:
        return
    as_of_date = parse_date(as_of)
    if as_of_date is None:
        return
    for line_no, cells in registry_rows:
        rid = cells[0]
        accessed = cells[5]
        acc_date = parse_date(accessed)
        if acc_date is None:
            continue
        if (as_of_date - acc_date).days > 180:
            findings.append(Finding(
                "WARN", "W_STALE",
                "source_registry.md row %d (%s): Accessed %s is more than "
                "180 days before as_of_date %s"
                % (line_no, rid, accessed, as_of)))


def check_contradiction_warn(claim_rows, findings):
    for c in claim_rows:
        if (c["contradicts"] and c["disposition"] == "include"
                and c["caveats"] in ("-", "")):
            findings.append(Finding(
                "WARN", "W_CONTRADICTION",
                "evidence_matrix.md row %d (%s): included claim with "
                "Contradicts set but no Caveats" % (c["line_no"], c["id"])))


def check_chart_warn(run_dir, findings):
    data_dir = os.path.join(run_dir, "data")
    if not os.path.isdir(data_dir):
        return
    for path in sorted(glob.glob(os.path.join(data_dir, "*.csv"))):
        has_meta = False
        try:
            text = read_text(path)
        except (OSError, UnicodeDecodeError):
            text = ""
        for line in text.splitlines():
            if line.strip().startswith("# source_ids:"):
                has_meta = True
                break
        if not has_meta:
            findings.append(Finding(
                "WARN", "W_CHART",
                "%s: missing '# source_ids:' metadata comment" % path))
    for path in sorted(glob.glob(os.path.join(data_dir, "*.json"))):
        has_meta = False
        try:
            data = json.loads(read_text(path))
            if isinstance(data, dict) and "source_ids" in data:
                has_meta = True
        except (OSError, UnicodeDecodeError, ValueError):
            has_meta = False
        if not has_meta:
            findings.append(Finding(
                "WARN", "W_CHART",
                "%s: missing top-level 'source_ids' key" % path))


NUM_TOKEN_RE = re.compile(r"\d+\.\d+|\d+")
# Citation markers such as [S64], [S01, S02] or a bare C12 are IDs, not data.
CITE_ID_RE = re.compile(r"\[(?:\s*[SC]\d{2,}\s*,?)+\]"
                        r"|(?<![A-Za-z0-9])[SC]\d{2,}(?![A-Za-z0-9])")


def extract_numeric_tokens(text):
    tokens = []
    text = CITE_ID_RE.sub(" ", text)
    for m in NUM_TOKEN_RE.finditer(text):
        numstr = m.group(0)
        try:
            val = float(numstr)
        except ValueError:
            continue
        if val < 10:
            continue
        if "." not in numstr and re.fullmatch(r"\d{4}", numstr):
            iv = int(numstr)
            if 1900 <= iv <= 2099:
                continue
        tokens.append(numstr)
    return tokens


def token_present(numstr, haystack):
    pattern = r"(?<![\d.])" + re.escape(numstr) + r"(?![\d.])"
    return re.search(pattern, haystack) is not None


def check_uncited_warn(run_dir, claim_rows, findings):
    nb_path = os.path.join(run_dir, "notebooklm_source.md")
    if not os.path.isfile(nb_path):
        return
    try:
        nb_text = read_text(nb_path)
    except (OSError, UnicodeDecodeError):
        return

    haystack_parts = []
    for c in claim_rows:
        haystack_parts.append(c["locator"])
    data_dir = os.path.join(run_dir, "data")
    if os.path.isdir(data_dir):
        for path in sorted(glob.glob(os.path.join(data_dir, "*.csv")) +
                            glob.glob(os.path.join(data_dir, "*.json"))):
            try:
                haystack_parts.append(read_text(path))
            except (OSError, UnicodeDecodeError):
                pass
    haystack = "\n".join(haystack_parts)

    tokens = extract_numeric_tokens(nb_text)
    seen = set()
    for tok in tokens:
        if tok in seen:
            continue
        seen.add(tok)
        if not token_present(tok, haystack):
            findings.append(Finding(
                "WARN", "W_UNCITED",
                "notebooklm_source.md: number '%s' not found in any Locator "
                "or data/*.csv|*.json content" % tok))


def validate_run(run_dir):
    """Returns (findings list, exit_code) for a RUN_DIR. Raises OSError-style
    signal via return code 2 tuple ('__IO__', 2) if run_dir itself missing."""
    findings = []
    if not os.path.isdir(run_dir):
        return (["error: RUN_DIR does not exist or is not a directory: %s"
                  % run_dir], 2)

    registry_path = os.path.join(run_dir, "source_registry.md")
    matrix_path = os.path.join(run_dir, "evidence_matrix.md")

    registry_rows = parse_table(registry_path, REGISTRY_HEADER, findings, "registry")
    matrix_rows = parse_table(matrix_path, MATRIX_HEADER, findings, "matrix")

    registry_ids = set()
    rows_by_id = {}
    if registry_rows is not None:
        registry_ids, rows_by_id = check_registry(registry_rows, findings)

    claim_rows = []
    if matrix_rows is not None:
        claim_rows = check_matrix(matrix_rows, registry_ids, findings)

    check_forecast_warn(claim_rows, findings)
    check_concentration_warn(claim_rows, findings)
    check_circular_warn(claim_rows, rows_by_id, findings)
    if registry_rows is not None:
        check_stale_warn(registry_rows, run_dir, findings)
    check_contradiction_warn(claim_rows, findings)
    check_chart_warn(run_dir, findings)
    check_uncited_warn(run_dir, claim_rows, findings)

    lines = [f.line() for f in findings]
    has_error = any(f.severity == "ERROR" for f in findings)
    return lines, (1 if has_error else 0)


# ---------------------------------------------------------------------------
# Selftest fixtures
# ---------------------------------------------------------------------------

def _reg(rows_text):
    return ("# Source registry\n\n" + REGISTRY_HEADER + "\n"
            + "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n"
            + rows_text)


def _mat(rows_text):
    return ("# Evidence matrix\n\n" + MATRIX_HEADER + "\n"
            + "|---|---|---|---|---|---|---|---|---|---|\n"
            + rows_text)


GOOD_REGISTRY = _reg(
    "| S01 | Good source | Org | https://example.org/a | 2026-01-01 | "
    "2026-08-01 | paper | primary | independent | A | imported | topic | "
    "- | - | 8 |\n"
)
GOOD_MATRIX = _mat(
    "| C01 | Something happened | observed | S01 | - | \"Table 1\" | metric "
    "| moderate | - | include |\n"
)

BAD_SCHEMA_MATRIX = "# Evidence matrix\n\n| Claim ID | Claim |\n|---|---|\n"

BAD_ID_MATRIX = _mat(
    "| C1 | Bad id format | observed | S01 | - | \"Table 1\" | metric | "
    "moderate | - | include |\n"
)

BAD_REF_MATRIX = _mat(
    "| C01 | References missing source | observed | S99 | - | \"Table 1\" "
    "| metric | moderate | - | include |\n"
)

BAD_ENUM_MATRIX = _mat(
    "| C01 | Bad class enum | observation | S01 | - | \"Table 1\" | metric "
    "| moderate | - | include |\n"
)

BAD_LOCATOR_MATRIX = _mat(
    "| C01 | Missing locator | observed | S01 | - | - | metric | moderate "
    "| - | include |\n"
)

BAD_LINEAGE_REGISTRY = _reg(
    "| S01 | Original | Org | https://example.org/a | 2026-01-01 | "
    "2026-08-01 | paper | primary | independent | A | imported | topic | "
    "- | - | 8 |\n"
    "| S02 | Derived | Org | https://example.org/b | 2026-01-01 | "
    "2026-08-01 | paper | secondary | independent | A | imported | topic | "
    "- | S77 | 4 |\n"
)

FORECAST_MATRIX = _mat(
    "| C01 | Growth continues | forecast | S01 | - | \"Table 1\" | metric "
    "| strong | - | include |\n"
)

CIRCULAR_REGISTRY = _reg(
    "| S01 | Original | Org | https://example.org/a | 2026-01-01 | "
    "2026-08-01 | paper | primary | independent | A | imported | topic | "
    "- | - | 8 |\n"
    "| S02 | Derived from S01 | Org | https://example.org/b | 2026-01-01 | "
    "2026-08-01 | paper | secondary | independent | A | imported | topic | "
    "- | S01 | 4 |\n"
)
CIRCULAR_MATRIX = _mat(
    "| C01 | Two related supports | interpretation | S01,S02 | - | "
    "\"Table 1\" | metric | moderate | - | include |\n"
)

UNCITED_NOTEBOOK = (
    "# Draft narrative\n\nThe survey found that 87% of respondents agreed.\n"
)


def build_selftest_fixtures(base_dir):
    fixtures = {}

    good = os.path.join(base_dir, "good_run")
    os.makedirs(good, exist_ok=True)
    with open(os.path.join(good, "source_registry.md"), "w", encoding="utf-8") as f:
        f.write(GOOD_REGISTRY)
    with open(os.path.join(good, "evidence_matrix.md"), "w", encoding="utf-8") as f:
        f.write(GOOD_MATRIX)
    fixtures["good_run"] = (good, 0, [], None)

    def make(name, registry_text, matrix_text, want_codes, extra=None):
        d = os.path.join(base_dir, name)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "source_registry.md"), "w", encoding="utf-8") as f:
            f.write(registry_text)
        with open(os.path.join(d, "evidence_matrix.md"), "w", encoding="utf-8") as f:
            f.write(matrix_text)
        if extra:
            extra(d)
        want_rc = 1 if any(c.startswith("E_") for c in want_codes) else 0
        fixtures[name] = (d, want_rc, want_codes, None)

    make("bad_schema_run", GOOD_REGISTRY, BAD_SCHEMA_MATRIX, ["E_SCHEMA"])
    make("bad_id_run", GOOD_REGISTRY, BAD_ID_MATRIX, ["E_ID"])
    make("bad_ref_run", GOOD_REGISTRY, BAD_REF_MATRIX, ["E_REF"])
    make("bad_enum_run", GOOD_REGISTRY, BAD_ENUM_MATRIX, ["E_ENUM"])
    make("bad_locator_run", GOOD_REGISTRY, BAD_LOCATOR_MATRIX, ["E_LOCATOR"])
    make("bad_lineage_run", BAD_LINEAGE_REGISTRY, GOOD_MATRIX, ["E_LINEAGE"])
    make("forecast_run", GOOD_REGISTRY, FORECAST_MATRIX, ["W_FORECAST"])
    make("circular_run", CIRCULAR_REGISTRY, CIRCULAR_MATRIX, ["W_CIRCULAR"])

    def add_bad_chart(d):
        data_dir = os.path.join(d, "data")
        os.makedirs(data_dir, exist_ok=True)
        with open(os.path.join(data_dir, "chart.csv"), "w", encoding="utf-8") as f:
            f.write("year,value\n2020,15\n2021,20\n")
    make("chart_run", GOOD_REGISTRY, GOOD_MATRIX, ["W_CHART"], extra=add_bad_chart)

    def add_uncited(d):
        with open(os.path.join(d, "notebooklm_source.md"), "w", encoding="utf-8") as f:
            f.write(UNCITED_NOTEBOOK)
    make("uncited_run", GOOD_REGISTRY, GOOD_MATRIX, ["W_UNCITED"], extra=add_uncited)

    return fixtures


def run_selftest():
    tmp = tempfile.mkdtemp(prefix="validate_evidence_selftest_")
    all_ok = True
    try:
        fixtures = build_selftest_fixtures(tmp)
        for name, (path, want_rc, want_codes, _unused) in fixtures.items():
            lines, rc = validate_run(path)
            ok = (rc == want_rc) and all(
                any(code in ln for ln in lines) for code in want_codes)
            status = "PASS" if ok else "FAIL"
            if not ok:
                all_ok = False
            print("%s: %s (rc=%d want=%d codes=%s)"
                  % (status, name, rc, want_rc, ",".join(want_codes) or "-"))
            for ln in lines:
                print("    %s" % ln)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return 0 if all_ok else 1


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="validate_evidence.py",
        description="Validate source_registry.md / evidence_matrix.md in a "
                     "deck-video research run directory.")
    parser.add_argument("run_dir", nargs="?", help="Path to the run directory")
    parser.add_argument("--selftest", action="store_true",
                         help="Run embedded fixture selftest and exit")
    args = parser.parse_args(argv)

    if args.selftest:
        sys.exit(run_selftest())

    if not args.run_dir:
        parser.error("RUN_DIR is required unless --selftest is given")

    lines, rc = validate_run(args.run_dir)
    for ln in lines:
        print(ln)
    sys.exit(rc)


if __name__ == "__main__":
    main()
