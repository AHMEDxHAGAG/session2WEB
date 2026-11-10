#!/usr/bin/env python3
"""Regenerate the other two project versions from the demo files.

  python3 make-stages.py

Inputs (the "non-accumulative" demo version — one block per patch):
  index.html, style.css

Outputs:
  final/            the full website: same code, all instructor banners
                    (▼ / ▲ / HOW TO DEMO) stripped — the clean answer key
  stages/patchN/    accumulative checkpoints: stage N = patches 1..N only
                    (stage 4 = the complete site, BONUS included)

Re-run this script any time you edit index.html / style.css.
"""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def strip_blocks(text: str, keep_up_to: int) -> str:
    """Drop every '▼ PATCH k' block (and the BONUS block, treated as k=4)
    whose k is greater than keep_up_to. Kept blocks pass through untouched."""
    out, skip, token = [], False, None
    for line in text.splitlines(keepends=True):
        if not skip:
            m = re.search(r"▼ (PATCH (\d+)|BONUS)", line)
            if m:
                token = m.group(1)
                k = int(m.group(2)) if m.group(2) else 4   # BONUS ships with patch 4
                if k > keep_up_to:
                    skip = True
                    continue
            out.append(line)
            continue
        if f"▲ END {token}" in line:
            skip = False
            token = None
        # lines inside a removed block are dropped (including its END banner)
    return "".join(out)


def clean_stage(text: str, kind: str) -> str:
    """Remove instructor scaffolding from stage output so students see
    a clean reference of what the page looks like after patch N.

    HTML: drop every comment (they are all instructor-only).
    CSS:  drop block-header comments (dividers / ▼ / ▲ / HOW TO DEMO)
          but keep property-level comments (they help students read the code).
    """
    pattern = r"<!--.*?-->" if kind == "html" else r"/\*.*?\*/"
    marker = re.compile(r"▼|▲|HOW TO DEMO|═══")
    text = re.sub(pattern, lambda m: "" if marker.search(m.group(0)) else m.group(0),
                  text, flags=re.S)
    # Drop orphaned divider opening/closing lines left behind when a block
    # was removed (e.g. a "/* ═════" whose "═════ */" was inside a deleted block).
    text = re.sub(r"^\s*/\*\s*═+\s*\n", "", text, flags=re.M)
    text = re.sub(r"^\s*═+\s*\*/\s*\n", "", text, flags=re.M)
    return re.sub(r"\n{3,}", "\n\n", text)


def clean_final(text: str, kind: str) -> str:
    """Remove instructor scaffolding comments, keep property comments."""
    pattern = r"<!--.*?-->" if kind == "html" else r"/\*.*?\*/"
    marker = re.compile(r"▼|▲|HOW TO DEMO")
    text = re.sub(pattern, lambda m: "" if marker.search(m.group(0)) else m.group(0),
                  text, flags=re.S)
    return re.sub(r"\n{3,}", "\n\n", text)


def main() -> None:
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    css = (ROOT / "style.css").read_text(encoding="utf-8")

    # ── Version 1: clean full website ────────────────────────────
    final = ROOT / "final"
    if final.exists():
        shutil.rmtree(final)
    (final / "assets").mkdir(parents=True)
    shutil.copy(ROOT / "assets/logo.svg", final / "assets/logo.svg")
    (final / "index.html").write_text(clean_final(html, "html"), encoding="utf-8")
    (final / "style.css").write_text(clean_final(css, "css"), encoding="utf-8")

    # ── Version 3: accumulative stages ───────────────────────────
    stages = ROOT / "stages"
    if stages.exists():
        shutil.rmtree(stages)
    for n in range(1, 5):
        d = stages / f"patch{n}"
        d.mkdir(parents=True)
        stage_html = strip_blocks(html, n)
        # stages sit two folders deep, so the <img> must climb back up
        stage_html = stage_html.replace('src="assets/logo.svg"',
                                        'src="../../assets/logo.svg"')
        (d / "index.html").write_text(clean_stage(stage_html, "html"),
                                      encoding="utf-8")
        (d / "style.css").write_text(clean_stage(strip_blocks(css, n), "css"),
                                     encoding="utf-8")

    print("final/ and stages/patch1..patch4 regenerated.")


if __name__ == "__main__":
    main()
