#!/usr/bin/env python
"""Remove the NotebookLM/Gemini Notebook watermark from an exported PPTX.

Each slide in a NotebookLM export is one full-bleed PNG; the watermark is baked
into the bottom-right pixels. This inpaints that region on every media image and
repacks the PPTX. Runs fully locally.

Usage:
  python clean_watermark.py in.pptx out.pptx [--box 0.855 0.952 0.999 0.998]
"""
import argparse, sys, zipfile
import cv2
import numpy as np


def clean(img_bytes: bytes, box, ext: str) -> bytes:
    arr = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)
    h, w = arr.shape[:2]
    x0, y0, x1, y1 = (int(w * box[0]), int(h * box[1]), int(w * box[2]), int(h * box[3]))
    mask = np.zeros((h, w), np.uint8)
    mask[y0:y1, x0:x1] = 255
    out = cv2.inpaint(arr, mask, 5, cv2.INPAINT_TELEA)
    # keep the source format so [Content_Types].xml stays truthful
    ok, buf = cv2.imencode("." + ext, out)
    assert ok
    return buf.tobytes()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--box", nargs=4, type=float, default=[0.855, 0.952, 0.999, 0.998],
                    help="watermark region as fractions: x0 y0 x1 y1")
    a = ap.parse_args()

    zin = zipfile.ZipFile(a.src)
    media = [n for n in zin.namelist()
             if n.startswith("ppt/media/image")
             and n.lower().rsplit(".", 1)[-1] in ("png", "jpg", "jpeg")]
    if not media:
        sys.exit("no media images found — is this a NotebookLM pptx export?")
    with zipfile.ZipFile(a.dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename in media:
                data = clean(data, a.box, item.filename.rsplit(".", 1)[1].lower())
                print("cleaned", item.filename)
            zout.writestr(item, data)
    print("wrote", a.dst)
    print("VERIFY: run render_review.py on the output and zoom the bottom-right "
          "corner of photo-background slides for inpaint smudges.")


if __name__ == "__main__":
    main()
