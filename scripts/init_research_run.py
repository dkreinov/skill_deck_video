#!/usr/bin/env python3
"""Initialize a deck-video research run directory with manifest and placeholders."""

import argparse
import json
import os
import sys
import re
import io
from datetime import datetime, timezone
from pathlib import Path


def derive_slug(topic: str) -> str:
    """Derive slug from topic according to spec.

    - lowercase
    - drop non-ASCII and punctuation
    - collapse whitespace runs to single hyphen
    - if > 40 chars, truncate at last hyphen at/before 40
    - strip leading/trailing hyphens
    """
    # lowercase
    s = topic.lower()

    # drop non-ASCII and punctuation, keep alphanumeric and spaces/hyphens
    s = re.sub(r'[^a-z0-9\s\-]', '', s)

    # collapse whitespace runs to single hyphen
    s = re.sub(r'\s+', '-', s)

    # if > 40 chars, truncate at last hyphen at or before position 40
    if len(s) > 40:
        # find the last hyphen at or before position 40
        truncated = s[:41]  # look at up to position 40 (0-indexed)
        last_hyphen_pos = truncated.rfind('-')
        if last_hyphen_pos > 0:
            s = s[:last_hyphen_pos]
        else:
            # no hyphen found, just truncate at 40
            s = s[:40]

    # strip leading/trailing hyphens
    s = s.strip('-')

    return s


def validate_date(date_str: str) -> bool:
    """Validate date matches YYYY-MM-DD and is a valid calendar date."""
    if not date_str:
        return False
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        return False
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def create_manifest(topic: str, slug: str, run_date: str) -> dict:
    """Create the run_manifest.json structure."""
    # Create ISO timestamp for created_at (current time in UTC)
    created_at = datetime.now(timezone.utc).isoformat()

    notebook_name = f"{run_date} — {slug} — deck-video"

    return {
        "project_title": topic,
        "topic_slug": slug,
        "created_at": created_at,
        "as_of_date": run_date,
        "forecast_horizon": None,
        "central_question": None,
        "initial_hypothesis": None,
        "approach_modes": [],
        "epistemic_posture": None,
        "audience": None,
        "deliverables": [],
        "intake": {
            "answers": {},
            "defaults_used": []
        },
        "notebook": {
            "name": notebook_name,
            "url": None,
            "created_fresh": True
        },
        "stage_status": {
            "intake": {"status": "pending", "updated_at": None},
            "research": {"status": "pending", "updated_at": None},
            "synthesis": {"status": "pending", "updated_at": None},
            "deck": {"status": "pending", "updated_at": None},
            "narration": {"status": "pending", "updated_at": None},
            "music": {"status": "pending", "updated_at": None},
            "qa": {"status": "pending", "updated_at": None}
        },
        "research_passes": [],
        "source_counts": {
            "imported": 0,
            "omitted": 0,
            "downloaded": 0
        },
        "artifacts": {},
        "blockers": []
    }


def create_placeholder_files(run_dir: str) -> list:
    """Create placeholder markdown files. Returns list of created paths."""
    paths = []

    # research_brief.md
    research_brief = """# Research brief

## Central question

## Definitions

## Hypotheses

## Evidence that would support

## Evidence that would weaken or falsify

## Research axes

## Source-quality policy

## Scope and dates

## Editorial approach and audience

## Excluded topics

## Expected output structure
"""
    path = os.path.join(run_dir, "research_brief.md")
    with io.open(path, 'w', encoding='utf-8') as f:
        f.write(research_brief)
    paths.append(path)

    # source_registry.md
    source_registry = """# Source registry

| ID | Title | Org/Author | URL | Pub date | Accessed | Type | Primary | Independent | Pass | Status | Topics | Caveats | Lineage | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
"""
    path = os.path.join(run_dir, "source_registry.md")
    with io.open(path, 'w', encoding='utf-8') as f:
        f.write(source_registry)
    paths.append(path)

    # evidence_matrix.md
    evidence_matrix = """# Evidence matrix

| Claim ID | Claim | Class | Supports | Contradicts | Locator | Metric | Confidence | Caveats | Disposition |
|---|---|---|---|---|---|---|---|---|---|
"""
    path = os.path.join(run_dir, "evidence_matrix.md")
    with io.open(path, 'w', encoding='utf-8') as f:
        f.write(evidence_matrix)
    paths.append(path)

    # research_checkpoint.md
    research_checkpoint = """# Research checkpoint

## Emerging answer

## Strongest supporting evidence

## Strongest counter-evidence

## Unresolved gaps

## Omitted claims

## Go/no-go
"""
    path = os.path.join(run_dir, "research_checkpoint.md")
    with io.open(path, 'w', encoding='utf-8') as f:
        f.write(research_checkpoint)
    paths.append(path)

    return paths


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a deck-video research run directory"
    )
    parser.add_argument("run_dir", help="Path to the run directory")
    parser.add_argument("--topic", required=True, help="Topic for the research")
    parser.add_argument("--slug", help="Slug for the topic (auto-derived if not provided)")
    parser.add_argument("--date", help="Run date in YYYY-MM-DD format (defaults to today)")

    args = parser.parse_args()

    run_dir = args.run_dir
    topic = args.topic
    slug = args.slug
    run_date = args.date

    # Derive slug if not provided
    if not slug:
        slug = derive_slug(topic)

    # Handle date
    if not run_date:
        run_date = datetime.now().strftime('%Y-%m-%d')

    # Validate date format
    if not validate_date(run_date):
        sys.stderr.write(f"error: invalid date format: {run_date} (must be YYYY-MM-DD)\n")
        sys.exit(2)

    # Check if RUN_DIR exists as a file (not directory)
    if os.path.exists(run_dir) and os.path.isfile(run_dir):
        sys.stderr.write(f"error: {run_dir} exists as a file, not a directory\n")
        sys.exit(2)

    # Check if run_manifest.json already exists
    manifest_path = os.path.join(run_dir, "run_manifest.json")
    if os.path.exists(manifest_path):
        sys.stderr.write(f"error: {manifest_path} already exists\n")
        sys.exit(2)

    try:
        # Create directory (parents ok)
        os.makedirs(run_dir, exist_ok=True)

        # Create manifest
        manifest = create_manifest(topic, slug, run_date)
        with io.open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)

        # Create placeholder files
        placeholder_paths = create_placeholder_files(run_dir)

        # Print output: notebook name and created paths
        notebook_name = manifest["notebook"]["name"]
        print(notebook_name)
        print(manifest_path)
        for path in placeholder_paths:
            print(path)

        sys.exit(0)

    except (OSError, IOError) as e:
        sys.stderr.write(f"error: {e}\n")
        sys.exit(2)


if __name__ == "__main__":
    main()
