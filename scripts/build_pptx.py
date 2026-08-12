#!/usr/bin/env python
"""Build a PPTX from N slide images (one full-bleed image per slide).

Uses deck_template.zip (shipped next to this script — masters/layouts/theme from
a known-good NotebookLM export, slides and media stripped) and generates the
slide parts for however many images are given. No third-party deps.

Usage:
  python build_pptx.py out.pptx slide_01.png slide_02.png ...
  python build_pptx.py out.pptx slides_dir/          # globs slide_*.png|jpg
"""
import glob, os, re, sys, zipfile

TEMPLATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "deck_template.zip")

SLIDE_XML = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
    'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
    'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
    '<p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>'
    '<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/>'
    '<a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>'
    '<p:pic><p:nvPicPr><p:cNvPr name="Slide image" id="2"/><p:cNvPicPr>'
    '<a:picLocks noChangeAspect="true"/></p:cNvPicPr><p:nvPr/></p:nvPicPr>'
    '<p:blipFill><a:blip r:embed="rId2"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>'
    '<p:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
    '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic>'
    '</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>'
)

SLIDE_RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Target="../slideLayouts/slideLayout7.xml" '
    'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout"/>'
    '<Relationship Id="rId2" Target="../media/image{i}.{ext}" '
    'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image"/>'
    '</Relationships>'
)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    out = sys.argv[1]
    args = sys.argv[2:]
    if len(args) == 1 and os.path.isdir(args[0]):
        images = sorted(glob.glob(os.path.join(args[0], "slide_*.png"))
                        + glob.glob(os.path.join(args[0], "slide_*.jpg"))
                        + glob.glob(os.path.join(args[0], "slide_*.jpeg")))
    else:
        images = args
    if not images:
        sys.exit("no slide images found")
    n = len(images)

    tpl = zipfile.ZipFile(TEMPLATE)
    pres = tpl.read("ppt/presentation.xml").decode()
    # slide size from template (e.g. cx=16256000 cy=9144000)
    m = re.search(r'<p:sldSz cx="(\d+)" cy="(\d+)"', pres)
    cx, cy = m.group(1), m.group(2)

    # regenerate slide id list: rIds start after existing non-slide rels
    pres_rels = tpl.read("ppt/_rels/presentation.xml.rels").decode()
    used = [int(x) for x in re.findall(r'Id="rId(\d+)"', pres_rels)]
    base = max(used) + 1
    sld_ids = "".join(f'<p:sldId id="{256+i}" r:id="rId{base+i}"/>' for i in range(n))
    pres = re.sub(r"<p:sldIdLst>.*?</p:sldIdLst>", f"<p:sldIdLst>{sld_ids}</p:sldIdLst>", pres, flags=re.S)
    new_rels = "".join(
        f'<Relationship Id="rId{base+i}" Target="slides/slide{i+1}.xml" '
        f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide"/>'
        for i in range(n))
    pres_rels = pres_rels.replace("</Relationships>", new_rels + "</Relationships>")

    ct = tpl.read("[Content_Types].xml").decode()
    overrides = "".join(
        f'<Override ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml" '
        f'PartName="/ppt/slides/slide{i+1}.xml"/>' for i in range(n))
    if 'Extension="jpg"' not in ct:
        ct = ct.replace("<Default", '<Default ContentType="image/jpeg" Extension="jpg"/><Default', 1)
    ct = ct.replace("</Types>", overrides + "</Types>")

    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for item in tpl.infolist():
            if item.filename in ("[Content_Types].xml", "ppt/presentation.xml",
                                 "ppt/_rels/presentation.xml.rels"):
                continue
            z.writestr(item, tpl.read(item.filename))
        z.writestr("[Content_Types].xml", ct)
        z.writestr("ppt/presentation.xml", pres)
        z.writestr("ppt/_rels/presentation.xml.rels", pres_rels)
        for i, img in enumerate(images):
            ext = img.rsplit(".", 1)[1].lower()
            z.writestr(f"ppt/media/image{i+1}.{ext}", open(img, "rb").read())
            z.writestr(f"ppt/slides/slide{i+1}.xml", SLIDE_XML.format(cx=cx, cy=cy))
            z.writestr(f"ppt/slides/_rels/slide{i+1}.xml.rels", SLIDE_RELS.format(i=i+1, ext=ext))
    print(f"wrote {out}: {n} slides")


if __name__ == "__main__":
    main()
