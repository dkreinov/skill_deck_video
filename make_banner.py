from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
BG = (15, 23, 42)        # slate-950 navy
FG = (241, 245, 249)     # near-white
MUT = (148, 163, 184)    # slate-400
AMB = (245, 158, 11)     # amber-500
GRID = (30, 41, 59)      # slate-800

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# subtle dot grid
for x in range(40, W, 44):
    for y in range(40, H, 44):
        d.ellipse([x, y, x + 2, y + 2], fill=GRID)

def font(name, size):
    return ImageFont.truetype(rf"C:\Windows\Fonts\{name}", size)

f_name  = font("segoeuib.ttf", 92)
f_tag   = font("segoeui.ttf", 34)
f_pipe  = font("consola.ttf", 26)
f_small = font("segoeui.ttf", 24)

X = 84
# small amber mark: three bars (deck) + play triangle (video)
d.rounded_rectangle([X, 96, X + 14, 146], 4, fill=AMB)
d.rounded_rectangle([X + 24, 110, X + 38, 146], 4, fill=(217, 119, 6))
d.rounded_rectangle([X + 48, 122, X + 62, 146], 4, fill=(180, 83, 9))
d.polygon([(X + 82, 108), (X + 82, 146), (X + 112, 127)], fill=FG)

# wordmark + tagline
d.text((X - 6, 180), "deck-video", font=f_name, fill=FG)
d.text((X, 320), "Fact-checked slide decks and narrated videos, from your sources.",
       font=f_tag, fill=MUT)

# pipeline line in monospace, amber accents on the gate
pipe_y = 425
parts = [("sources", MUT), ("  ->  ", GRID2 := (71, 85, 105)), ("research", MUT),
         ("  ->  ", GRID2), ("fact gate", AMB), ("  ->  ", GRID2), ("deck", MUT),
         ("  ->  ", GRID2), ("narration + music", MUT), ("  ->  ", GRID2), ("video", FG)]
x = X
for text, color in parts:
    d.text((x, pipe_y), text, font=f_pipe, fill=color)
    x += d.textlength(text, font=f_pipe)

# footer
d.text((X, 540), "A Claude Code skill  ·  NotebookLM slides  ·  local TTS + mixing  ·  everything verified against sources",
       font=f_small, fill=(100, 116, 139))

# thin amber baseline accent
d.rectangle([X, 500, X + 320, 503], fill=AMB)

img.save("assets/banner.png")
print("saved", img.size)
