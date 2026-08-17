# -*- coding: utf-8 -*-
"""Deterministic DATA CHART renderer for the singularity_report deck.

Every quantitative slide in the deck is rendered here from the CSV files in this
directory - never by an image generator. Each CSV carries `# source_ids:` plus the
metric definition, units/denominator, dataset version, date range, transformation and
this render command, per the deck-video DATA CHART contract.

Palette and typography are taken from the deck's Global visual direction block in
`slide_division.md` - background #0B0E14, primary #D7DEE8, muted #6E7A8A, and ONE
accent #E8A33D whose fixed meaning is "the single measured thing that decides this
slide's claim". Everything else is grey. No matplotlib defaults, no legends, no
gridlines beyond a hairline value grid, zero-based value axes, direct labels.

Output: 1376x768 PNG files sized to drop straight into the deck's slide images.

Usage:
    python charts/render_charts.py            # render all
    python charts/render_charts.py <name>     # render one
"""
import csv
import io
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
W, H, DPI = 1376, 768, 100

# --- deck style block ---
BG = "#0B0E14"      # near-black field, identical on every slide
FG = "#D7DEE8"      # pale grey: primary marks and headline type
MUTED = "#6E7A8A"   # muted slate: secondary marks, axes, captions
ACCENT = "#E8A33D"  # amber: the one measured thing that decides the claim
GRID = "#1A2029"    # hairline value grid

SANS = ["DejaVu Sans"]
MONO = ["DejaVu Sans Mono"]


def _read(name):
    with io.open(os.path.join(HERE, name), encoding="utf-8") as fh:
        lines = [l for l in fh if not l.lstrip().startswith("#")]
    return list(csv.DictReader(lines))


def _fig():
    return plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=BG)


def _frame(fig, title, subtitle, source):
    """Assertion at the top, provenance at the bottom, generous margins."""
    fig.text(0.06, 0.93, title, color=FG, fontsize=31, fontweight="light",
             family=SANS, va="top")
    fig.text(0.06, 0.855, subtitle, color=MUTED, fontsize=14.5, family=SANS, va="top")
    fig.text(0.06, 0.045, source, color=MUTED, fontsize=10.5, family=MONO, va="bottom")


def _axes(fig, rect):
    ax = fig.add_axes(rect)
    ax.set_facecolor(BG)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=MUTED, labelsize=12.5)
    for lbl in ax.get_xticklabels() + ax.get_yticklabels():
        lbl.set_family(MONO)
    return ax


def _note(fig, x, y, text, color=MUTED, size=13.5):
    fig.text(x, y, text, color=color, fontsize=size, family=SANS, va="top")


def _save(fig, name):
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, name + ".png")
    fig.savefig(path, facecolor=BG)
    plt.close(fig)
    print("wrote", path)


def task_horizon_doubling():
    """Accent: the post-2024 bar. The shrinking interval IS the claim."""
    rows = _read("task_horizon_doubling.csv")
    vals = [float(r["doubling_days"]) for r in rows]
    tags = [r["doubling_months_label"] for r in rows]
    names = ["2019-2025\nbaseline", "post-2023\ncohort", "post-2024\ncohort"]
    colors = [MUTED, MUTED, ACCENT]

    fig = _fig()
    _frame(fig,
           "The capability clock is speeding up",
           "Days for the 50%-success task horizon to double, by model cohort.",
           "METR, Time Horizon 1.1 (2026-01-29) [S56] · 228 tasks · cohort splits are post-hoc")
    ax = _axes(fig, [0.19, 0.20, 0.50, 0.55])
    bars = ax.barh(range(len(vals)), vals, color=colors, height=0.46)
    ax.set_yticks(range(len(vals)))
    ax.set_yticklabels(names, color=FG, fontsize=13, family=SANS)
    ax.invert_yaxis()
    ax.set_xlabel("days per doubling", color=MUTED, fontsize=12.5, family=MONO)
    ax.set_xlim(0, 230)
    ax.xaxis.grid(True, color=GRID, linewidth=1)
    ax.set_axisbelow(True)
    for b, v, t, c in zip(bars, vals, tags, colors):
        ax.text(v + 6, b.get_y() + b.get_height() / 2, "%.1f  (%s)" % (v, t),
                color=c if c == ACCENT else FG, fontsize=13, family=MONO, va="center")
    _note(fig, 0.735, 0.62, "Each step now\narrives sooner\nthan the last.", FG, 14.5)
    _note(fig, 0.735, 0.40, "This is capability\nprogress, not the\nrate of AI R&D.")
    _save(fig, "task_horizon_doubling")


def reliability_gap():
    """Accent: both 80%-success bars. The strict bar governs unattended work."""
    rows = _read("reliability_gap.csv")
    order = ["public frontier models", "internal frontier configs"]
    fifty = [float(r["hours"]) for r in rows if r["threshold"] == "50% success"]
    eighty = [float(r["hours"]) for r in rows if r["threshold"] == "80% success"]
    lab50 = [r["label"] for r in rows if r["threshold"] == "50% success"]
    lab80 = [r["label"] for r in rows if r["threshold"] == "80% success"]

    fig = _fig()
    _frame(fig,
           "Ask for reliability and the horizon collapses",
           "Hours of human-expert task time an agent completes autonomously, at two success bars.",
           "METR, Frontier Risk Report Feb-Mar 2026, published 2026-05-19 [S89] · internal values are floors")
    ax = _axes(fig, [0.10, 0.21, 0.82, 0.53])
    x, w = [0, 1], 0.26
    b1 = ax.bar([i - w / 2 for i in x], fifty, width=w, color=MUTED)
    b2 = ax.bar([i + w / 2 for i in x], eighty, width=w, color=ACCENT)
    ax.set_xticks(x)
    ax.set_xticklabels(order, color=FG, fontsize=14.5, family=SANS)
    ax.set_ylabel("hours", color=MUTED, fontsize=12.5, family=MONO)
    ax.set_ylim(0, 23)
    ax.yaxis.grid(True, color=GRID, linewidth=1)
    ax.set_axisbelow(True)
    for b, t in zip(b1, lab50):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.5,
                t + "  50%", color=MUTED, fontsize=12.5, family=MONO, ha="center")
    for b, t in zip(b2, lab80):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.5,
                t + "  80%", color=ACCENT, fontsize=12.5, family=MONO, ha="center")
    fig.text(0.50, 0.125,
             "Unattended R&D needs the amber bar, not the grey one.",
             color=FG, fontsize=14.5, family=SANS, ha="center")
    _save(fig, "reliability_gap")


def benchmark_vs_reality():
    """Accent: the human-maintainer bar - the measurement that contradicts the benchmark."""
    rows = _read("benchmark_vs_reality.csv")
    vals = [float(r["value_pct"]) for r in rows]
    dens = [r["denominator"] for r in rows]
    names = ["automated grader", "human maintainers", "held-out repos"]
    colors = [MUTED, ACCENT, MUTED]

    fig = _fig()
    _frame(fig,
           "The benchmark and the maintainer disagree",
           "Success rate under three different graders. Three different denominators.",
           "METR maintainer study of 296 PRs, 2026-03-10 [S23] · SWE-bench Pro figure via [S03]")
    ax = _axes(fig, [0.22, 0.25, 0.45, 0.49])
    bars = ax.barh(range(len(vals)), vals, color=colors, height=0.42)
    ax.set_yticks(range(len(vals)))
    ax.set_yticklabels(names, color=FG, fontsize=14, family=SANS)
    ax.invert_yaxis()
    ax.set_xlabel("success rate (%)", color=MUTED, fontsize=12.5, family=MONO)
    ax.set_xlim(0, 100)
    ax.xaxis.grid(True, color=GRID, linewidth=1)
    ax.set_axisbelow(True)
    for b, v, d, c in zip(bars, vals, dens, colors):
        y = b.get_y() + b.get_height() / 2
        ax.text(v + 2.5, y, "%.1f%%" % v,
                color=c if c == ACCENT else FG, fontsize=15, family=MONO, va="center")
        ax.text(2.5, y + 0.36, "of " + d, color=MUTED, fontsize=10, family=MONO, va="center")
    _note(fig, 0.70, 0.63,
          "Maintainers rejected\nabout half the pull\nrequests that had\nalready passed the\nautomated grader.", FG, 14)
    _note(fig, 0.70, 0.32, "Not a decline over\ntime - three separate\nmeasurements.")
    _save(fig, "benchmark_vs_reality")


def forecast_disagreement():
    """Accent: the by-2030 pair. The nine-fold gap is the message."""
    rows = _read("forecast_disagreement.csv")
    cohorts = [r["cohort"].lower() for r in rows]
    y2030 = [float(r["by_2030_pct"]) for r in rows]
    y2050 = [float(r["by_2050_pct"]) for r in rows]

    fig = _fig()
    _frame(fig,
           "The forecasters do not agree with each other",
           "Elicited probability of transformative AI. This measures belief, not capability.",
           "Forecasting Research Institute elicitation, 2023 [S46] · reported via [S52], lineage [S54]")
    ax = _axes(fig, [0.10, 0.21, 0.82, 0.53])
    x, w = [0, 1], 0.26
    b1 = ax.bar([i - w / 2 for i in x], y2030, width=w, color=ACCENT)
    b2 = ax.bar([i + w / 2 for i in x], y2050, width=w, color=MUTED)
    ax.set_xticks(x)
    ax.set_xticklabels(cohorts, color=FG, fontsize=14.5, family=SANS)
    ax.set_ylabel("probability (%)", color=MUTED, fontsize=12.5, family=MONO)
    ax.set_ylim(0, 56)
    ax.yaxis.grid(True, color=GRID, linewidth=1)
    ax.set_axisbelow(True)
    for b, v in zip(b1, y2030):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.1, "%d%%  by 2030" % v,
                color=ACCENT, fontsize=12.5, family=MONO, ha="center")
    for b, v in zip(b2, y2050):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.1, "%d%%  by 2050" % v,
                color=MUTED, fontsize=12.5, family=MONO, ha="center")
    fig.text(0.50, 0.125,
             "Same question, same year: a nine-fold gap by 2030.",
             color=FG, fontsize=14.5, family=SANS, ha="center")
    _save(fig, "forecast_disagreement")


CHARTS = {
    "task_horizon_doubling": task_horizon_doubling,
    "reliability_gap": reliability_gap,
    "benchmark_vs_reality": benchmark_vs_reality,
    "forecast_disagreement": forecast_disagreement,
}

if __name__ == "__main__":
    for n in (sys.argv[1:] or list(CHARTS)):
        CHARTS[n]()
