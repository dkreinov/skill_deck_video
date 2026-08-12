#!/usr/bin/env python
"""Build a narrated slide video from a narration script + slide PNGs.

Script format: markdown with one `## Slide N — title` heading per slide; the
block body is the spoken text. Slide images: slide_01.png, slide_02.png, ... in
slides_dir (use render_review.py to produce them). Each slide is shown for
lead + measured-narration + tail seconds — sync is correct by construction.

Usage:
  python build_narration.py narration_script.md slides_dir out.mp4
         [--voice en-US-AndrewMultilingualNeural] [--rate -4%]
         [--lead 0.6] [--tail 1.0] [--workdir build]
  python build_narration.py --samples narration_script.md   # 3-voice audition
"""
import argparse, asyncio, glob, hashlib, os, re, subprocess, sys

VOICES = {
    "andrew": "en-US-AndrewMultilingualNeural",
    "ava": "en-US-AvaMultilingualNeural",
    "brian": "en-US-BrianMultilingualNeural",
}


def parse_script(path):
    text = open(path, encoding="utf-8").read()
    blocks = re.split(r"^## Slide \d+.*$", text, flags=re.M)[1:]
    lines = [re.sub(r"^#.*$", "", b, flags=re.M).strip() for b in blocks]
    if not lines:
        sys.exit("no '## Slide N' blocks found in script")
    return lines


def ffmpeg():
    from imageio_ffmpeg import get_ffmpeg_exe
    return get_ffmpeg_exe()


def dur(ff, path):
    r = subprocess.run([ff, "-i", path, "-f", "null", "-"], capture_output=True, text=True)
    # Prefer the container header. The decode-progress "time=" lines under-report
    # on concatenated MP4s (observed: 389.1s reported for a 573.8s output), which
    # silently misstates the final runtime.
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
    if m:
        h, mn, s = m.groups()
        return int(h) * 3600 + int(mn) * 60 + float(s)
    m = re.findall(r"time=(\d+):(\d+):([\d.]+)", r.stderr)
    h, mn, s = m[-1]
    return int(h) * 3600 + int(mn) * 60 + float(s)


async def tts(text, voice, rate, out):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate=rate).save(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("slides_dir", nargs="?")
    ap.add_argument("out", nargs="?")
    ap.add_argument("--voice", default=VOICES["andrew"])
    ap.add_argument("--rate", default="-4%")
    ap.add_argument("--lead", type=float, default=0.6)
    ap.add_argument("--tail", type=float, default=1.0)
    ap.add_argument("--workdir", default="build")
    ap.add_argument("--pad-color", default="0x1b2635",
                    help="letterbox color behind non-16:9 slides")
    ap.add_argument("--samples", action="store_true",
                    help="write voice_sample_{andrew,ava,brian}.mp3 of slide 2 and exit")
    a = ap.parse_args()

    lines = parse_script(a.script)
    os.makedirs(a.workdir, exist_ok=True)

    if a.samples:
        probe = lines[1] if len(lines) > 1 else lines[0]
        for name, v in VOICES.items():
            out = os.path.join(a.workdir, f"voice_sample_{name}.mp3")
            asyncio.run(tts(probe, v, a.rate, out))
            print("sample:", out)
        return

    if not (a.slides_dir and a.out):
        sys.exit("slides_dir and out.mp4 required (or use --samples)")
    slides = sorted(glob.glob(os.path.join(a.slides_dir, "slide_*.png")))
    assert len(slides) == len(lines), f"{len(slides)} slides vs {len(lines)} script blocks"

    ff = ffmpeg()
    segs = []
    for i, (text, png) in enumerate(zip(lines, slides), 1):
        # hash text into the cache name so edited narration regenerates audio
        h = hashlib.sha1((a.voice + a.rate + text).encode("utf-8")).hexdigest()[:10]
        mp3 = os.path.join(a.workdir, f"seg_{i:02d}_{h}.mp3")
        if not os.path.exists(mp3):
            asyncio.run(tts(text, a.voice, a.rate, mp3))
        d = dur(ff, mp3)
        total = a.lead + d + a.tail
        seg = os.path.join(a.workdir, f"vseg_{i:02d}.mp4")
        cmd = [ff, "-y",
               "-loop", "1", "-framerate", "30", "-i", png,
               "-i", mp3,
               "-filter_complex",
               f"[0:v]scale=1920:1080:force_original_aspect_ratio=decrease:flags=lanczos,"
               f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color={a.pad_color},"
               f"format=yuv420p[v];"
               f"[1:a]adelay={int(a.lead*1000)}|{int(a.lead*1000)},apad=pad_dur={a.tail},aresample=48000[a]",
               "-map", "[v]", "-map", "[a]",
               "-t", f"{total:.2f}",
               "-c:v", "libx264", "-preset", "medium", "-crf", "18",
               "-c:a", "aac", "-b:a", "192k", seg]
        r = subprocess.run(cmd, capture_output=True, text=True)
        assert r.returncode == 0, r.stderr[-1500:]
        segs.append(seg)
        print(f"slide {i}: narration {d:.1f}s -> {total:.1f}s")

    lst = os.path.join(a.workdir, "concat.txt")
    with open(lst, "w") as f:
        for s in segs:
            f.write(f"file '{os.path.abspath(s)}'\n")
    r = subprocess.run([ff, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", a.out],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[-1500:]
    print(f"FINAL {a.out}: {dur(ff, a.out):.1f}s")


if __name__ == "__main__":
    main()
