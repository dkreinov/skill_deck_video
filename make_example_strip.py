from PIL import Image
import os

# four real slides from the example run, as a filmstrip
SRC = r"C:\Users\dkreinov\AppData\Local\Temp\claude\C--Users-dkreinov-claude-shiri-presentation\fab3c35b-4e43-4a21-8250-6a9abc32e655\scratchpad\ksec"
picks = ["slide_01.png", "slide_07.png", "slide_11.png", "slide_16.png"]
GAP, W = 8, 1280
tile_w = (W - GAP * (len(picks) - 1)) // len(picks)

tiles = []
for p in picks:
    im = Image.open(os.path.join(SRC, p))
    ratio = tile_w / im.width
    tiles.append(im.resize((tile_w, int(im.height * ratio)), Image.LANCZOS))

h = tiles[0].height
strip = Image.new("RGB", (W, h), (15, 23, 42))
x = 0
for t in tiles:
    strip.paste(t, (x, 0))
    x += tile_w + GAP
strip.save("assets/example_slides.png")
print("saved", strip.size)
