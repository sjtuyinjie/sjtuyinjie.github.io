#!/usr/bin/env python3
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "images" / "2026_tacbpm.png"
ARXIV = "https://arxiv.org/html/2609.18174v1/figures"
SITE = "https://tacbpm.github.io/static/videos/tacbfp"
VID_CACHE = Path("/tmp/tacbpm_grid")

GAP = 5
MARGIN_LEFT = 30
MARGIN_OTHER = 4
MARGIN_TOP = 13
IMG_W = 198
IMG_H = 132
CAP_H = 20
BG = (252, 252, 253)
LINE = (203, 213, 225)
CAPTION_COLOR = (71, 85, 105)
BADGE_BG = (241, 245, 249)
BADGE_FG = (30, 41, 59)
BADGE_EDGE = (148, 163, 184)
AXIS_FG = (100, 116, 139)

QUADS = (
    (
        0,
        0,
        [
            (f"{ARXIV}/qualitative/tiles/prior_multiobject_b_object_overlays_filled.png", "paper", "Sphere teachers"),
            (f"{ARXIV}/qualitative/tiles/prior_multiobject_a_object_overlays.png", "paper", "Downstream mix"),
            (f"{ARXIV}/qualitative/tiles/downstream_a_block03_object_overlay.png", "paper", "Block transfer"),
            (f"{ARXIV}/qualitative/tiles/downstream_b_block05_object_overlay.png", "paper", "Hard block"),
        ],
    ),
    (
        0,
        2,
        [
            ("small_hammer.mp4", "sim", "Small hammer"),
            ("blue_brush.mp4", "sim", "Blue brush"),
            ("staples_marker.mp4", "sim", "Staples marker"),
            ("mallet_hammer.mp4", "sim", "Mallet hammer"),
        ],
    ),
    (
        2,
        0,
        [
            (f"{ARXIV}/qualitative/tiles/real_a_small_tennis.png", "paper", "Small tennis"),
            (f"{ARXIV}/qualitative/tiles/real_c_standard_tennis.png", "paper", "Std tennis"),
            (f"{ARXIV}/qualitative/tiles/real_d_corner_block.png", "paper", "Corner block"),
            (f"{ARXIV}/qualitative/tiles/real_e_multiface.png", "paper", "Multiface"),
        ],
    ),
    (
        2,
        2,
        [
            ("seq1_h264.mp4", "real3", "Real grasp"),
            ("seq2_h264.mp4", "real3", "Real lift"),
            ("seq3_h264.mp4", "real3", "Real reorient"),
            ("seq4_h264.mp4", "real3", "Real deploy"),
        ],
    ),
)


def fetch(url: str, dest: Path) -> None:
    subprocess.run(["curl", "-fsSL", "-o", str(dest), url], check=True)


def frame_at(vpath: Path, t: float, dest: Path) -> None:
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-ss",
            f"{t:.3f}",
            "-i",
            str(vpath),
            "-frames:v",
            "1",
            "-q:v",
            "2",
            str(dest),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def video_mid(vpath: Path, dest: Path) -> None:
    probe = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(vpath),
        ],
        text=True,
    ).strip()
    t = max(0.1, float(probe) / 2.0)
    frame_at(vpath, t, dest)


def resolve_image(src: str, kind: str, td: Path, index: int) -> Path:
    out = td / f"tile_{index}.jpg"
    if kind == "paper":
        tmp = td / f"tile_{index}.png"
        fetch(src, tmp)
        return tmp
    vpath = VID_CACHE / src
    sub = "arm/sim" if kind == "sim" else "arm/grasp_repose_real"
    if not vpath.is_file():
        vpath.parent.mkdir(parents=True, exist_ok=True)
        fetch(f"{SITE}/{sub}/{src}", vpath)
    if kind == "sim":
        video_mid(vpath, out)
    else:
        frame_at(vpath, 3.0, out)
    return out


def cover_crop(path: Path) -> Image.Image:
    img = Image.open(path).convert("RGB")
    w, h = img.size
    scale = max(IMG_W / w, IMG_H / h)
    nw, nh = int(w * scale), int(h * scale)
    img = img.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - IMG_W) // 2
    top = (nh - IMG_H) // 2
    return img.crop((left, top, left + IMG_W, top + IMG_H))


def font(size: int = 11) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for name in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/TTF/DejaVuSans.ttf",
    ):
        p = Path(name)
        if p.is_file():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


def make_tile(img: Image.Image, caption: str) -> Image.Image:
    tile = Image.new("RGB", (IMG_W, IMG_H + CAP_H), BG)
    tile.paste(img, (0, 0))
    draw = ImageDraw.Draw(tile)
    fnt = font(11)
    bbox = draw.textbbox((0, 0), caption, font=fnt)
    tw = bbox[2] - bbox[0]
    draw.text(((IMG_W - tw) // 2, IMG_H + 3), caption, fill=CAPTION_COLOR, font=fnt)
    return tile


def tile_origin(row: int, col: int) -> tuple[int, int]:
    x = MARGIN_LEFT + col * (IMG_W + GAP)
    y = MARGIN_OTHER + MARGIN_TOP + row * (IMG_H + CAP_H + GAP)
    return x, y


def draw_badge(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, fnt) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pad_x, pad_y = 6, 3
    draw.rounded_rectangle(
        [x, y, x + tw + pad_x * 2, y + th + pad_y * 2],
        radius=4,
        fill=BADGE_BG,
        outline=BADGE_EDGE,
        width=1,
    )
    draw.text((x + pad_x, y + pad_y - 1), text, fill=BADGE_FG, font=fnt)


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        td = Path(tmp)
        tiles: list[tuple[int, int, Image.Image]] = []
        idx = 0
        for row0, col0, items in QUADS:
            for i, (src, kind, cap) in enumerate(items):
                path = resolve_image(src, kind, td, idx)
                img = cover_crop(path)
                tile = make_tile(img, cap)
                r = row0 + i // 2
                c = col0 + i % 2
                tiles.append((r, c, tile))
                idx += 1

        grid_w = 4 * IMG_W + 3 * GAP + MARGIN_LEFT + MARGIN_OTHER
        grid_h = 4 * (IMG_H + CAP_H) + 3 * GAP + MARGIN_OTHER * 2 + MARGIN_TOP
        out = Image.new("RGB", (grid_w, grid_h), BG)
        draw = ImageDraw.Draw(out)

        for r, c, tile in tiles:
            out.paste(tile, tile_origin(r, c))

        x0, y0 = MARGIN_LEFT, MARGIN_OTHER + MARGIN_TOP
        x1 = MARGIN_LEFT + 4 * IMG_W + 3 * GAP
        y1 = MARGIN_OTHER + MARGIN_TOP + 4 * (IMG_H + CAP_H) + 3 * GAP
        x_mid = MARGIN_LEFT + 2 * IMG_W + GAP + GAP // 2
        y_mid = MARGIN_OTHER + MARGIN_TOP + 2 * (IMG_H + CAP_H + GAP) + GAP // 2
        quad_w = 2 * IMG_W + GAP

        draw.rectangle([x0, y0, x1, y1], outline=LINE, width=1)
        draw.line([(x_mid, y0), (x_mid, y1)], fill=LINE, width=2)
        draw.line([(x0, y_mid), (x1, y_mid)], fill=LINE, width=2)

        axis_fnt = font(12)
        inhand, armhand, sim, real = "In-hand", "Arm-hand", "Sim", "Real"
        ih_bb = draw.textbbox((0, 0), inhand, font=axis_fnt)
        ah_bb = draw.textbbox((0, 0), armhand, font=axis_fnt)
        sim_bb = draw.textbbox((0, 0), sim, font=axis_fnt)
        real_bb = draw.textbbox((0, 0), real, font=axis_fnt)
        ih_w, ah_w = ih_bb[2] - ih_bb[0], ah_bb[2] - ah_bb[0]
        sim_w, real_w = sim_bb[2] - sim_bb[0], real_bb[2] - real_bb[0]

        draw.text(
            (x0 + quad_w // 2 - ih_w // 2, MARGIN_OTHER),
            inhand,
            fill=AXIS_FG,
            font=axis_fnt,
        )
        draw.text(
            (x_mid + quad_w // 2 - ah_w // 2, MARGIN_OTHER),
            armhand,
            fill=AXIS_FG,
            font=axis_fnt,
        )
        draw.text((6, y0 + (y_mid - y0) // 2 - 6), sim, fill=AXIS_FG, font=axis_fnt)
        draw.text((4, y_mid + (y1 - y_mid) // 2 - 6), real, fill=AXIS_FG, font=axis_fnt)

        tag_fnt = font(10)
        draw_badge(draw, x0 + 3, y0 + 3, "In-hand · Sim", tag_fnt)
        draw_badge(draw, x_mid + 3, y0 + 3, "Arm-hand · Sim", tag_fnt)
        draw_badge(draw, x0 + 3, y_mid + 3, "In-hand · Real", tag_fnt)
        draw_badge(draw, x_mid + 3, y_mid + 3, "Arm-hand · Real", tag_fnt)

        OUT.parent.mkdir(parents=True, exist_ok=True)
        out.save(OUT, format="PNG", optimize=True)
        print(OUT, out.size)


if __name__ == "__main__":
    main()