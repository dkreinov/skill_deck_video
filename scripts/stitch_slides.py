"""Stitch two-pass native-resolution slide captures back into 1376x768 PNGs.

Why two passes: the claude-in-chrome `zoom` region is measured in SCREENSHOT
BUFFER pixels, and the buffer is the viewport downscaled to a 1568px-wide cap.
With a maximized 1920x855 window the scale is 1568/1920 = 0.81667, so the buffer
is only ~698 rows tall -- less than a slide's 768. Rendering the slide at
1685x940 CSS makes it land at exactly 1376x768 buffer px (1:1 with native), but
it no longer fits vertically, so it is captured in two vertically-shifted passes
and stitched here.

Pass A: overlay top = 0px    -> slide rows 0..690
Pass B: overlay top = -96px  -> slide rows ~78..768

The exact offset is recovered by cross-correlating the overlap rather than
trusting the arithmetic, because the zoom output is resampled.
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

REGION_W, REGION_H = 1376, 690   # what we asked zoom for, in buffer px
NATIVE_W, NATIVE_H = 1376, 768   # true slide size


def load_region(path):
    """Zoom upscales its output; bring it back to the true region size."""
    im = Image.open(path).convert("RGB")
    if im.size != (REGION_W, REGION_H):
        im = im.resize((REGION_W, REGION_H), Image.LANCZOS)
    return np.asarray(im, dtype=np.float32)


def best_offset(a, b, lo=60, hi=110):
    """Find d minimising |a[d:] - b[:-d]| -- i.e. B is A shifted up by d rows."""
    best, best_err = None, float("inf")
    for d in range(lo, hi + 1):
        overlap = REGION_H - d
        if overlap < 200:
            continue
        err = np.abs(a[d:d + overlap] - b[:overlap]).mean()
        if err < best_err:
            best, best_err = d, err
    return best, best_err


def strip_backdrop(out):
    """Replace rows/cols showing the magenta capture backdrop.

    The overlay is sized so the slide lands at exactly 1376x768 buffer px, but
    sub-pixel rounding can leave the outermost row or column short, exposing the
    backdrop. Those edge lines are replaced by their nearest clean neighbour,
    which is visually exact at the frame edge.
    """
    r, g, b = out[:, :, 0], out[:, :, 1], out[:, :, 2]
    mag = (r > 100) & (b > 100) & (g < r * 0.6) & (g < b * 0.6)

    bad_rows = np.where(mag.mean(axis=1) > 0.5)[0]
    clean_rows = [i for i in range(out.shape[0]) if i not in set(bad_rows)]
    for i in bad_rows:
        src = min(clean_rows, key=lambda j: abs(j - i))
        out[i] = out[src]

    bad_cols = np.where(mag.mean(axis=0) > 0.5)[0]
    clean_cols = [i for i in range(out.shape[1]) if i not in set(bad_cols)]
    for i in bad_cols:
        src = min(clean_cols, key=lambda j: abs(j - i))
        out[:, i] = out[:, src]

    return out, len(bad_rows), len(bad_cols)


def stitch(path_a, path_b, out_path):
    a = load_region(path_a)
    b = load_region(path_b)

    d, err = best_offset(a, b)
    if d is None:
        raise SystemExit(f"no valid offset for {out_path}")

    out = np.zeros((NATIVE_H, NATIVE_W, 3), dtype=np.float32)
    out[:REGION_H] = a                       # rows 0..690 from pass A
    tail = NATIVE_H - REGION_H               # 78 rows still missing
    out[REGION_H:] = b[REGION_H - d:REGION_H - d + tail]

    out, nr, nc = strip_backdrop(out)

    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(out_path)
    return d, err, nr, nc


if __name__ == "__main__":
    if len(sys.argv) == 4:
        d, err, nr, nc = stitch(sys.argv[1], sys.argv[2], sys.argv[3])
        print(f"offset={d} err={err:.2f} edge_rows={nr} edge_cols={nc} -> {sys.argv[3]}")
    else:
        # batch mode: stitch_slides.py <capture_dir> <out_dir>
        cap, out = Path(sys.argv[1]), Path(sys.argv[2])
        out.mkdir(parents=True, exist_ok=True)
        for i in range(1, 17):
            pa = cap / f"slide_{i:02d}_A.png"
            pb = cap / f"slide_{i:02d}_B.png"
            if not (pa.exists() and pb.exists()):
                print(f"skip {i}: missing pass")
                continue
            d, err, nr, nc = stitch(pa, pb, out / f"slide_{i:02d}.png")
            print(f"slide {i:02d}: offset={d} err={err:.2f} edge_rows={nr} edge_cols={nc}")
