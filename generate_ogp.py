"""
風雅舎 ブログOGP画像 ジェネレーター

使い方:
  python3 generate_ogp.py

CATEGORIES から category を選び、TITLE_LINES に見出しを1〜3行で指定して実行すると、
/home/claude/ogp/output/ に 1200x630 の完成OGP画像(PNG)が書き出されます。

タイトルは日本語の自動折り返しができないため、TITLE_LINES に手動で行分けして渡してください。
1行あたり全角14〜16文字程度が目安です。
"""

import subprocess
import os

CATEGORIES = {
    "ai-dx": {
        "label_ja": "AI導入・業務効率化",
        "label_en": "AI / DX",
        "mid": "#1c3c58",
        "top": "#5a7a90",
        "glow": "#e8866a",
    },
    "security": {
        "label_ja": "セキュリティ",
        "label_en": "SECURITY",
        "mid": "#3a2440",
        "top": "#6b4a5c",
        "glow": "#a85a52",
    },
    "design-brand": {
        "label_ja": "デザイン・ブランディング",
        "label_en": "DESIGN",
        "mid": "#4a3038",
        "top": "#b97a5e",
        "glow": "#e8a866",
    },
    "work-style": {
        "label_ja": "経営・働き方",
        "label_en": "WORK STYLE",
        "mid": "#362f48",
        "top": "#7a7590",
        "glow": "#c48ba0",
    },
}

SVG_TEMPLATE = """<svg width="1200" height="630" viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0%" stop-color="#0a1a28"/>
      <stop offset="55%" stop-color="{mid}"/>
      <stop offset="100%" stop-color="{top}"/>
    </linearGradient>
    <radialGradient id="dawn" cx="82%" cy="88%" r="60%">
      <stop offset="0%" stop-color="{glow}" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="{glow}" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="28"/>
    </filter>
    <filter id="grain" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" stitchTiles="stitch" result="n"/>
      <feColorMatrix in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.045 0"/>
    </filter>
  </defs>

  <rect width="1200" height="630" fill="url(#sky)"/>
  <rect width="1200" height="630" fill="url(#dawn)"/>

  <g filter="url(#soft)">
    <ellipse cx="920" cy="520" rx="420" ry="60" fill="{top}" opacity="0.18"/>
    <ellipse cx="1050" cy="440" rx="340" ry="50" fill="#f0e6d6" opacity="0.12"/>
    <ellipse cx="250" cy="460" rx="360" ry="60" fill="#c8d8e2" opacity="0.12"/>
    <ellipse cx="600" cy="150" rx="280" ry="45" fill="#f0e6d6" opacity="0.06"/>
  </g>

  <rect width="1200" height="630" filter="url(#grain)"/>

  <!-- category label -->
  <text x="90" y="150" font-family="Noto Sans CJK JP" font-size="20" font-weight="500"
        letter-spacing="3" fill="{glow}">{label_en}</text>

  <!-- title -->
  <text font-family="Noto Serif CJK JP" font-weight="500" font-size="58" fill="#f0e6d6">
{title_tspans}
  </text>

  <!-- brand mark -->
  <text x="90" y="560" font-family="Noto Sans CJK JP" font-size="18" font-weight="400"
        letter-spacing="2" fill="#f0e6d6" opacity="0.6">風雅舎 / FUGASHA</text>
</svg>
"""


def build_title_tspans(lines, start_x=90, start_y=230, line_height=74):
    tspans = []
    for i, line in enumerate(lines):
        y = start_y + i * line_height
        tspans.append(f'    <tspan x="{start_x}" y="{y}">{line}</tspan>')
    return "\n".join(tspans)


def generate(category_key, title_lines, out_name):
    cat = CATEGORIES[category_key]
    svg = SVG_TEMPLATE.format(
        mid=cat["mid"],
        top=cat["top"],
        glow=cat["glow"],
        label_en=cat["label_en"],
        title_tspans=build_title_tspans(title_lines),
    )
    os.makedirs("/home/claude/ogp/output", exist_ok=True)
    svg_path = f"/home/claude/ogp/output/{out_name}.svg"
    png_path = f"/home/claude/ogp/output/{out_name}.png"
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    subprocess.run(["rsvg-convert", "-w", "1200", "-h", "630", svg_path, "-o", png_path], check=True)
    print("generated:", png_path)


if __name__ == "__main__":
    # 例: セキュリティカテゴリの1本目記事（仮タイトル）
    generate(
        "security",
        ["中小企業のための、", "AIセキュリティ入門"],
        "example-security-01",
    )
