#!/usr/bin/env python
"""Remove the NotebookLM/Gemini Notebook watermark from a directory of slide PNGs.

Companion to clean_watermark.py, which operates on a PPTX. Use this one when the
slides were captured from the NotebookLM viewer (see capture_slides notes in
SKILL.md) rather than downloaded as a deck, i.e. when you already have
slide_01.png..slide_NN.png on disk.

Usage:
  python clean_watermark_png.py slides_dir out_dir [--box 0.855 0.952 0.999 0.998]

Verify afterwards by eyeballing the bottom-right corner of any slide whose
background is a photo or a dense illustration -- INPAINT_TELEA can smudge there.
On flat dark backgrounds (the usual case for these decks) it is invisible.
"""
import argparse
from pathlib import Path

import cv2
import numpy as np


def clean_file(src: Path, dst: Path, box) -> tuple[int, int]:
    arr = cv2.imread(str(src), cv2.IMREAD_COLOR)
    if arr is None:
        raise SystemExit(f"could not read {src}")
    h, w = arr.shape[:2]
    x0, y0, x1, y1 = (int(w * box[0]), int(h * box[1]), int(w * box[2]), int(h * box[3]))
    mask = np.zeros((h, w), np.uint8)
    mask[y0:y1, x0:x1] = 255
    out = cv2.inpaint(arr, mask, 5, cv2.INPAINT_TELEA)
    cv2.imwrite(str(dst), out)
    return w, h


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src_dir")
    ap.add_argument("dst_dir")
    ap.add_argument("--box", nargs=4, type=float,
                    default=[0.855, 0.952, 0.999, 0.998],
                    help="watermark region as fractions of width/height: x0 y0 x1 y1")
    a = ap.parse_args()

    src_dir, dst_dir = Path(a.src_dir), Path(a.dst_dir)
    dst_dir.mkdir(parents=True, exist_ok=True)

    pngs = sorted(src_dir.glob("slide_*.png"))
    if not pngs:
        raise SystemExit(f"no slide_*.png found in {src_dir}")

    for p in pngs:
        w, h = clean_file(p, dst_dir / p.name, a.box)
        print(f"cleaned {p.name} ({w}x{h})")
    print(f"wrote {len(pngs)} slides -> {dst_dir}")


if __name__ == "__main__":
    main()
