#!/usr/bin/env python
"""Build a narrated slide video from a narration script + slide PNGs.

Script format: markdown with one `## Slide N — title` heading per slide; the
block body is the spoken text. Slide images: slide_01.png, slide_02.png, ... in
slides_dir (use render_review.py to produce them). Each slide is shown for
lead + measured-narration + tail seconds — sync is correct by construction.

Engines:
  edge        — Microsoft edge-tts neural voices, free/unlimited (default)
  elevenlabs  — ElevenLabs REST API; needs a key (--key-file or
                ELEVENLABS_API_KEY). Free tier: premade voices only, 10k
                chars/month. Segments are cached by text hash, so edits
                re-bill only the changed slides.

Usage:
  python build_narration.py narration_script.md slides_dir out.mp4
         [--lang en] [--voice V] [--rate -4%] [--engine edge|elevenlabs]
         [--model eleven_v3] [--key-file path] [--max-chars 10000]
         [--lead 0.6] [--tail 1.0] [--workdir build]
  python build_narration.py --samples narration_script.md --lang he
         # audition every mapped voice for that language (edge engine only)
"""
import argparse, asyncio, glob, hashlib, json, os, re, subprocess, sys
import urllib.request

# Per-language edge-tts voices (male/female pairs; first entry = default).
# More: python -m edge_tts --list-voices | grep -i <code>
LANG_VOICES = {
    "en": ["en-US-AndrewMultilingualNeural", "en-US-AvaMultilingualNeural",
           "en-US-BrianMultilingualNeural"],
    "he": ["he-IL-AvriNeural", "he-IL-HilaNeural"],
    "ar": ["ar-EG-ShakirNeural", "ar-EG-SalmaNeural", "ar-SA-HamedNeural"],
    "ru": ["ru-RU-DmitryNeural", "ru-RU-SvetlanaNeural"],
    "de": ["de-DE-ConradNeural", "de-DE-KatjaNeural"],
    "fr": ["fr-FR-HenriNeural", "fr-FR-DeniseNeural"],
    "es": ["es-ES-AlvaroNeural", "es-ES-ElviraNeural"],
}
ELEVENLABS_DEFAULT_VOICE = "EXAVITQu4vr4xnSDxMaL"  # Sarah (premade, free tier)


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


async def edge_tts_save(text, voice, rate, out):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate=rate).save(out)


def elevenlabs_key(key_file):
    if key_file:
        return open(key_file, encoding="utf-8").read().strip()
    key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not key:
        sys.exit("elevenlabs engine needs --key-file or ELEVENLABS_API_KEY")
    return key


def elevenlabs_tts(text, voice, model, key, out):
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice}",
        data=json.dumps({"text": text, "model_id": model}).encode("utf-8"),
        headers={"xi-api-key": key, "Content-Type": "application/json"})
    try:
        audio = urllib.request.urlopen(req).read()
    except urllib.error.HTTPError as e:
        # 402 on library voices (free tier is premade-only) and 401 on cloned
        # voices without a paid plan are the common failures; neither bills.
        sys.exit(f"elevenlabs HTTP {e.code}: {e.read().decode(errors='replace')[:300]}")
    with open(out, "wb") as f:
        f.write(audio)


def render_segment(a, text, key, out):
    if a.engine == "elevenlabs":
        elevenlabs_tts(text, a.voice, a.model, key, out)
    else:
        asyncio.run(edge_tts_save(text, a.voice, a.rate, out))


def srt_time(t):
    ms = int(round(t * 1000))
    return f"{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}"


def slide_captions(text, start, dur_s):
    """Sentence-level captions, timed proportionally to sentence length.

    Proportional timing tracks real TTS pacing within a couple hundred ms —
    good enough for slide narration; exact word timing would need forced
    alignment, which this pipeline deliberately avoids.
    """
    sentences = [s for s in re.split(r"(?<=[.!?…])\s+", text.replace("\n", " ")) if s.strip()]
    total = sum(len(s) for s in sentences) or 1
    out, cursor = [], start
    for s in sentences:
        d = dur_s * len(s) / total
        out.append((cursor, cursor + d, s.strip()))
        cursor += d
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("slides_dir", nargs="?")
    ap.add_argument("out", nargs="?")
    ap.add_argument("--lang", default="en",
                    help="narration language code; picks the default voice "
                         f"({', '.join(LANG_VOICES)})")
    ap.add_argument("--voice", default=None,
                    help="edge-tts voice name, or ElevenLabs voice ID")
    ap.add_argument("--rate", default="-4%", help="edge engine only")
    ap.add_argument("--engine", choices=["edge", "elevenlabs"], default="edge")
    ap.add_argument("--model", default="eleven_v3",
                    help="elevenlabs model (eleven_v3 is the Hebrew-capable one)")
    ap.add_argument("--key-file", default=None,
                    help="file whose only line is the ElevenLabs API key")
    ap.add_argument("--max-chars", type=int, default=10000,
                    help="refuse to send more than this many NEW (uncached) chars "
                         "to elevenlabs; 0 = unlimited")
    ap.add_argument("--lead", type=float, default=0.6)
    ap.add_argument("--tail", type=float, default=1.0)
    ap.add_argument("--workdir", default="build")
    ap.add_argument("--pad-color", default="0x1b2635",
                    help="letterbox color behind non-16:9 slides")
    ap.add_argument("--samples", action="store_true",
                    help="write voice samples of slide 2 for --lang and exit (edge only)")
    ap.add_argument("--no-srt", action="store_true",
                    help="skip the sidecar .srt subtitle file (written next to out.mp4 "
                         "by default; never burned into the video)")
    a = ap.parse_args()

    if a.lang not in LANG_VOICES and not a.voice:
        sys.exit(f"no voice map for --lang {a.lang}; pass --voice explicitly "
                 "(python -m edge_tts --list-voices)")
    if not a.voice:
        a.voice = ELEVENLABS_DEFAULT_VOICE if a.engine == "elevenlabs" \
            else LANG_VOICES[a.lang][0]

    lines = parse_script(a.script)
    os.makedirs(a.workdir, exist_ok=True)

    if a.samples:
        if a.engine == "elevenlabs":
            sys.exit("--samples is edge-only (elevenlabs samples cost credits; "
                     "audition voices at elevenlabs.io instead)")
        probe = lines[1] if len(lines) > 1 else lines[0]
        for v in LANG_VOICES.get(a.lang, [a.voice]):
            out = os.path.join(a.workdir, f"voice_sample_{v}.mp3")
            asyncio.run(edge_tts_save(probe, v, a.rate, out))
            print("sample:", out)
        return

    if not (a.slides_dir and a.out):
        sys.exit("slides_dir and out.mp4 required (or use --samples)")
    slides = sorted(glob.glob(os.path.join(a.slides_dir, "slide_*.png")))
    assert len(slides) == len(lines), f"{len(slides)} slides vs {len(lines)} script blocks"

    key = elevenlabs_key(a.key_file) if a.engine == "elevenlabs" else None

    # hash engine+voice+model+rate+text into the cache name so edited narration
    # (or a changed voice) regenerates audio — and unchanged slides never re-bill
    def seg_path(i, text):
        stamp = f"{a.engine}|{a.voice}|{a.model if a.engine == 'elevenlabs' else a.rate}|{text}"
        h = hashlib.sha1(stamp.encode("utf-8")).hexdigest()[:10]
        return os.path.join(a.workdir, f"seg_{i:02d}_{h}.mp3")

    if a.engine == "elevenlabs":
        new_chars = sum(len(t) for i, t in enumerate(lines, 1)
                        if not os.path.exists(seg_path(i, t)))
        cached = len(lines) - sum(1 for i, t in enumerate(lines, 1)
                                  if not os.path.exists(seg_path(i, t)))
        print(f"elevenlabs: {new_chars} new chars to bill ({cached} segments cached)")
        if a.max_chars and new_chars > a.max_chars:
            sys.exit(f"refusing: {new_chars} chars exceeds --max-chars {a.max_chars} "
                     "(raise the cap explicitly if the credits are available)")

    ff = ffmpeg()
    segs, captions, clock = [], [], 0.0
    for i, (text, png) in enumerate(zip(lines, slides), 1):
        mp3 = seg_path(i, text)
        if not os.path.exists(mp3):
            render_segment(a, text, key, mp3)
        d = dur(ff, mp3)
        total = a.lead + d + a.tail
        captions += slide_captions(text, clock + a.lead, d)
        clock += total
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
    if not a.no_srt:
        srt = os.path.splitext(a.out)[0] + ".srt"
        with open(srt, "w", encoding="utf-8") as f:
            for n, (t0, t1, s) in enumerate(captions, 1):
                f.write(f"{n}\n{srt_time(t0)} --> {srt_time(t1)}\n{s}\n\n")
        print(f"subtitles: {srt} ({len(captions)} cues, sidecar — drop the file to drop them)")
    print(f"FINAL {a.out}: {dur(ff, a.out):.1f}s")


if __name__ == "__main__":
    main()
