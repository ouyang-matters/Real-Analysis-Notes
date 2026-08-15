#!/usr/bin/env python3
"""Generate Real Analysis series cover images (EN + ZH) in 1:1 and 2.35:1."""
import subprocess, os, glob

COVERS_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(COVERS_DIR, exist_ok=True)
os.chdir(COVERS_DIR)

OUT_DIR = os.path.join(os.path.dirname(COVERS_DIR), 'pdf', 'covers')
os.makedirs(OUT_DIR, exist_ok=True)

SERIES_NAME_EN = "Real Analysis"
SERIES_NAME_ZH = "实分析"

# (numeral, en_title, zh_title, authors, date_en, date_zh)
ARTICLES = [
    ("Sup",
     "Uniform Integrability and the\\\\Vitali Convergence Theorem",
     "一致可积性与 $L^1$ 收敛",
     "A.~Ouyang", "August 2026", "2026年8月"),
]


def make_cover(numeral, title, authors, date, series_name,
               width_cm, height_cm, is_zh=False,
               hex_cx_frac=0.7, hex_cy_frac=0.65, hex_r=5.0,
               title_size=18, title_lead=23, numeral_size=44,
               title_width_frac=0.65, series_size=6,
               numeral_xshift=-0.8, numeral_yshift=0.6,
               author_size=8, title_y_frac=0.33, author_y_offset=1.2,
               date_size=7):

    # CJK preamble for Chinese covers
    if is_zh:
        font_pkg = r"""\usepackage{xeCJK}
\setCJKmainfont{Noto Serif CJK SC}
\setCJKsansfont{Noto Sans CJK SC}"""
    else:
        font_pkg = r"\usepackage{newtxtext}"

    hex_cx = width_cm * hex_cx_frac
    hex_cy = height_cm * hex_cy_frac

    return (r"""\documentclass[border=0pt]{standalone}
\usepackage{tikz}
\usepackage{xcolor}
""" + font_pkg + r"""

\definecolor{ra-orange}{HTML}{CC5500}
\definecolor{ra-tint}{HTML}{F5DCC8}
\definecolor{article-text}{HTML}{1A1A2E}
\definecolor{article-muted}{HTML}{888888}
\definecolor{bg}{HTML}{FBF8F4}

\begin{document}
\begin{tikzpicture}

%% Background
\fill[bg] (0,0) rectangle ("""
    + f"{width_cm}cm,{height_cm}cm"
    + r""");

%% Tinted hexagon
\clip (0,0) rectangle ("""
    + f"{width_cm}cm,{height_cm}cm"
    + r""");
\fill[ra-tint, opacity=0.8, rotate around={15:("""
    + f"{hex_cx}cm,{hex_cy}cm"
    + r""")}]
  ("""
    + f"{hex_cx}cm,{hex_cy}cm"
    + r""") ++(0:"""
    + f"{hex_r}cm"
    + r""") \foreach \a in {60,120,...,300} { -- +(\a:"""
    + f"{hex_r}cm"
    + r""") } -- cycle;

%% Series name
\node[anchor=north west, font=\sffamily\fontsize{"""
    + f"{series_size}"
    + r"""}{"""
    + f"{series_size + 2}"
    + r"""}\selectfont, text=article-muted]
  at ("""
    + f"1.2cm,{height_cm - 0.8}cm"
    + r""") {\MakeUppercase{"""
    + series_name
    + r"""}};

%% Article title
\node[anchor=south west, text width="""
    + f"{width_cm * title_width_frac}cm"
    + r""",
  font=\fontsize{"""
    + f"{title_size}"
    + r"""}{"""
    + f"{title_lead}"
    + r"""}\selectfont,
  text=article-text, align=left]
  at ("""
    + f"1.2cm,{height_cm * title_y_frac}cm"
    + r""") {"""
    + title
    + r"""};

%% Author
\node[anchor=south west,
  font=\fontsize{"""
    + f"{author_size}"
    + r"""}{"""
    + f"{author_size + 3}"
    + r"""}\selectfont,
  text=article-muted]
  at ("""
    + f"1.2cm,{height_cm * title_y_frac - author_y_offset}cm"
    + r""") {"""
    + authors
    + r"""};

%% Date
\node[anchor=south west,
  font=\fontsize{"""
    + f"{date_size}"
    + r"""}{"""
    + f"{date_size + 3}"
    + r"""}\selectfont,
  text=article-muted]
  at ("""
    + f"1.2cm,{height_cm * title_y_frac - author_y_offset - 1.0}cm"
    + r""") {"""
    + date
    + r"""};

%% Numeral
\node[anchor=south east,
  font=\fontsize{"""
    + f"{numeral_size}"
    + r"""}{"""
    + f"{numeral_size}"
    + r"""}\selectfont,
  text=article-text!80]
  at ([xshift="""
    + f"{numeral_xshift}cm, yshift={numeral_yshift}cm] {width_cm}cm,0cm"
    + r""") {"""
    + numeral
    + r"""};

\end{tikzpicture}
\end{document}
""")


# Generate all covers
for numeral, title_en, title_zh, authors, date_en, date_zh in ARTICLES:
    tag = numeral.lower()

    for lang, title, date, series, is_zh in [
        ("en", title_en, date_en, SERIES_NAME_EN, False),
        ("zh", title_zh, date_zh, SERIES_NAME_EN, True),
    ]:
        # 1:1 square
        w, h = 10.8, 10.8
        tex = make_cover(numeral, title, authors, date, series,
            width_cm=w, height_cm=h, is_zh=is_zh,
            hex_cx_frac=0.64, hex_cy_frac=0.70, hex_r=6.2,
            title_size=18, title_lead=24, numeral_size=44,
            title_width_frac=0.65, series_size=6,
            numeral_xshift=-0.8, numeral_yshift=0.6,
            author_size=8, title_y_frac=0.33, author_y_offset=1.2,
            date_size=7)
        fname = f"cover_{tag}_1x1_{lang}.tex"
        with open(fname, 'w') as f:
            f.write(tex)

        # 2.35:1 wide
        w, h = 23.5, 10.0
        tex = make_cover(numeral, title, authors, date, series,
            width_cm=w, height_cm=h, is_zh=is_zh,
            hex_cx_frac=0.67, hex_cy_frac=0.68, hex_r=8.0,
            title_size=20, title_lead=27, numeral_size=50,
            title_width_frac=0.45, series_size=7,
            numeral_xshift=-1.0, numeral_yshift=0.6,
            author_size=9, title_y_frac=0.33, author_y_offset=1.3,
            date_size=8)
        fname = f"cover_{tag}_wide_{lang}.tex"
        with open(fname, 'w') as f:
            f.write(tex)

print("Generated .tex files")

# Compile
for tex_file in sorted(glob.glob("cover_*.tex")):
    base = tex_file[:-4]
    compiler = "xelatex" if "_zh" in tex_file else "pdflatex"
    print(f"Compiling {base} ({compiler})...", end=" ", flush=True)
    r = subprocess.run([compiler, "-interaction=nonstopmode", tex_file],
                       capture_output=True, text=True)
    if os.path.exists(f"{base}.pdf"):
        print("OK")
    else:
        print("FAILED")
        for line in r.stdout.split('\n'):
            if line.startswith('!'):
                print(f"  {line}")

# Convert to PNG
for pdf in sorted(glob.glob("cover_*.pdf")):
    base = pdf[:-4]
    parts = base.split('_')  # cover_sup_1x1_en / cover_sup_wide_zh
    tag = parts[1]
    ratio = 'square' if parts[2] == '1x1' else 'wide'
    lang = parts[3]
    out_name = f"ra-{tag}-{ratio}-{lang}.png"

    subprocess.run(["pdftoppm", "-png", "-r", "300", "-singlefile", pdf,
                    f"/tmp/_ra_cover_tmp"], capture_output=True)
    src = "/tmp/_ra_cover_tmp.png"
    dst = f"{OUT_DIR}/{out_name}"
    if os.path.exists(src):
        os.rename(src, dst)
    print(f"  -> {dst}")

# Clean build artifacts
for ext in ('aux', 'log', 'pdf', 'tex'):
    for f in glob.glob(f"cover_*.{ext}"):
        os.remove(f)

print("\nDone!")
