#!/usr/bin/env python
"""Render a deck (pptx or pdf) to per-slide PNGs for the Fact Gate review.

For a NotebookLM PPTX (one full-bleed image per slide) the media images are
extracted directly via the slide rels, preserving order. For a PDF, pages are
rendered with PyMuPDF.

Usage:
  python render_review.py deck.pptx outdir/
  python render_review.py deck.pdf  outdir/ [--dpi 110]
"""
import argparse, os, re, zipfile


def from_pptx(src, outdir):
    import cv2
    import numpy as np
    z = zipfile.ZipFile(src)
    n_slides = len([n for n in z.namelist()
                    if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)])
    for i in range(1, n_slides + 1):
        rels = z.read(f"ppt/slides/_rels/slide{i}.xml.rels").decode()
        m = re.search(r"media/(image\d+\.\w+)", rels)
        if not m:
            raise SystemExit(
                f"slide {i} has no image rel — this deck is not a one-image-"
                "per-slide export; render the PDF instead")
        data = z.read(f"ppt/media/{m.group(1)}")
        # normalize to PNG so downstream tools (build_narration) find slide_*.png
        out = os.path.join(outdir, f"slide_{i:02d}.png")
        if m.group(1).lower().endswith(".png"):
            with open(out, "wb") as f:
                f.write(data)
        else:
            arr = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
            cv2.imwrite(out, arr)
    return n_slides


def from_pdf(src, outdir, dpi):
    import fitz
    doc = fitz.open(src)
    for i, page in enumerate(doc):
        page.get_pixmap(dpi=dpi).save(os.path.join(outdir, f"slide_{i+1:02d}.png"))
    return len(doc)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("outdir")
    ap.add_argument("--dpi", type=int, default=110)
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    if a.src.lower().endswith(".pptx"):
        n = from_pptx(a.src, a.outdir)
    else:
        n = from_pdf(a.src, a.outdir, a.dpi)
    print(f"{n} slides -> {a.outdir}")
    print("FACT GATE: read every PNG. Check numbers vs source doc, names/orders, "
          "text INSIDE imagery (garbles, invalid data), 'identical' panels that "
          "differ, brand-lookalike imagery, meaning-inverting phrasing.")


if __name__ == "__main__":
    main()
