#!/usr/bin/env python
"""Mix a music bed under a narrated video, or analyze candidate tracks.

Analyze (pick the steadier background bed — lower loudness-stddev, longer wins):
  python mix_music.py --analyze a.mp3 b.mp3 ...

Mix (video stream copied untouched; music auto-gained to the bed target,
lowpass 10 kHz, fade in 2s / out 5s, looped to cover the video):
  python mix_music.py video.mp4 music.mp3 out.mp4 [--bed-db -25]

Bed guidance: -25 dB = clearly audible (laptop speakers); -35 dB = subtle.
Produce both variants for the user by default.
"""
import argparse, re, statistics, subprocess, sys


def ffmpeg():
    from imageio_ffmpeg import get_ffmpeg_exe
    return get_ffmpeg_exe()


def duration(ff, path):
    r = subprocess.run([ff, "-i", path, "-f", "null", "-"], capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


def mean_vol(ff, path, ss=None, t=None):
    cmd = [ff]
    if ss is not None:
        cmd += ["-ss", str(ss)]
    if t is not None:
        cmd += ["-t", str(t)]
    cmd += ["-i", path, "-af", "volumedetect", "-f", "null", "-"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    d = dict(re.findall(r"(mean_volume|max_volume): (-?[\d.]+) dB", r.stderr))
    return float(d.get("mean_volume", "nan")), float(d.get("max_volume", "nan"))


def analyze(ff, paths):
    for p in paths:
        r = subprocess.run([ff, "-i", p, "-af", "ebur128=metadata=0", "-f", "null", "-"],
                           capture_output=True, text=True)
        momentary = [float(m) for m in re.findall(r"M:\s*(-?[\d.]+)", r.stderr) if float(m) > -70]
        sd = statistics.pstdev(momentary) if momentary else float("nan")
        print(f"{p}: {duration(ff, p):.0f}s  loudness-stddev {sd:.2f} dB  "
              f"(lower = steadier bed)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+")
    ap.add_argument("--analyze", action="store_true")
    ap.add_argument("--bed-db", type=float, default=-25.0)
    ap.add_argument("--gap-ss", type=float, default=None,
                    help="timestamp of a known music-only moment for the level "
                    "check (e.g. a slide-boundary gap); omit to skip that check")
    a = ap.parse_args()
    ff = ffmpeg()

    if a.analyze:
        analyze(ff, a.inputs)
        return
    if len(a.inputs) != 3:
        sys.exit("usage: mix_music.py video.mp4 music.mp3 out.mp4 [--bed-db -25]")
    vid, mus, out = a.inputs

    vdur = duration(ff, vid)
    mmean, _ = mean_vol(ff, mus)
    gain = 10 ** ((a.bed_db - mmean) / 20)
    print(f"video {vdur:.1f}s; music mean {mmean:.1f} dB -> gain {gain:.3f} "
          f"(bed target {a.bed_db} dB)")

    cmd = [ff, "-y",
           "-i", vid,
           "-stream_loop", "-1", "-i", mus,
           "-filter_complex",
           f"[1:a]volume={gain:.4f},lowpass=f=10000,afade=t=in:d=2,"
           f"afade=t=out:st={max(0, vdur-5)}:d=5,aresample=48000[m];"
           f"[0:a][m]amix=inputs=2:duration=first:normalize=0[a]",
           "-map", "0:v", "-c:v", "copy",
           "-map", "[a]", "-c:a", "aac", "-b:a", "192k",
           "-t", str(vdur), out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[-1500:]

    if a.gap_ss is not None:
        gap = mean_vol(ff, out, ss=a.gap_ss, t=1.3)
        print(f"music-only gap mean/max: {gap} (want approx. bed target)")
    speech = mean_vol(ff, out, ss=min(30, vdur / 2), t=5)
    print(f"speech region mean/max:  {speech} (peaks should sit >=10 dB above bed)")
    print("wrote", out)


if __name__ == "__main__":
    main()
