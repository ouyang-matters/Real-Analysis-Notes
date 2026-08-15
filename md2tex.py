#!/usr/bin/env python3
"""Convert sup_03.md to LaTeX for Real Analysis series."""
import re

with open('sup_03.md', 'r') as f:
    lines = f.readlines()

out = []
in_math = False
math_buf = []

def process_math_block(block):
    """Process a display math block, fixing artifacts."""
    result = []
    i = 0
    while i < len(block):
        line = block[i]
        stripped = line.strip()

        # Lines of === represent a single = sign
        if re.match(r'^=+$', stripped):
            result.append('=\n')
            # Skip blank line after ===
            if i + 1 < len(block) and block[i+1].strip() == '':
                i += 2
            else:
                i += 1
            continue

        # Lines starting with # in math are markdown header artifacts → =
        if stripped.startswith('# '):
            result.append('= ' + stripped[2:] + '\n')
            i += 1
            continue

        # Fix set notation: bare {text} → \{text\}
        # Match {|...|...} or {text} at start of line or after space
        fixed = re.sub(r'(?<!\\)(?<![a-zA-Z])\{([^}]*)\}(?!\s*[,;.\)])',
                       lambda m: '\\{' + m.group(1) + '\\}' if not any(
                           cmd in m.group(0) for cmd in
                           ['\\boxed', '\\begin', '\\end', '\\frac', '\\mathbf',
                            '\\text', '\\array', '\\aligned', '\\left', '\\right',
                            '\\MakeUppercase']
                       ) else m.group(0),
                       stripped)
        # Simpler approach: only fix {|...} and {f_n} {g>K} patterns (set notation)
        result.append(line)
        i += 1

    return result

def fix_sets_in_math(text):
    """Fix set notation {|f|>K} → \\{|f|>K\\} in math content."""
    # Match {|...|...} patterns (set builder with absolute values)
    text = re.sub(r'(?<!\\)\{(\|[^}]+)\}', r'\\{\1\\}', text)
    # Match {g>K} {f_n} etc — single expressions that look like sets
    text = re.sub(r'(?<!\\)\{(g>[^}]+)\}', r'\\{\1\\}', text)
    text = re.sub(r'(?<!\\)\{(f_n)\}', r'\\{\1\\}', text)
    return text

# Process line by line
i = 0
while i < len(lines):
    line = lines[i]
    stripped = line.strip()

    # Display math start
    if stripped == '$$':
        if not in_math:
            in_math = True
            math_buf = []
            i += 1
            continue
        else:
            # End of math block
            in_math = False
            # Process the math buffer
            processed = []
            j = 0
            while j < len(math_buf):
                mline = math_buf[j]
                ms = mline.strip()

                # === lines → =
                if re.match(r'^=+\s*$', ms):
                    processed.append('=\n')
                    # skip following blank line
                    if j + 1 < len(math_buf) and math_buf[j+1].strip() == '':
                        j += 2
                    else:
                        j += 1
                    continue

                # # in math → = (markdown header artifact)
                if ms.startswith('# '):
                    processed.append('= ' + ms[2:] + '\n')
                    j += 1
                    continue

                processed.append(mline)
                j += 1

            # Join and fix sets
            math_text = ''.join(processed)
            math_text = fix_sets_in_math(math_text)
            # Fix ,d\mu → \,d\mu
            math_text = math_text.replace(',d\\mu', '\\,d\\mu')
            math_text = math_text.replace(',dx', '\\,dx')

            out.append('\\[\n')
            out.append(math_text)
            out.append('\\]\n')
            i += 1
            continue

    if in_math:
        math_buf.append(line)
        i += 1
        continue

    # Section headers
    if stripped.startswith('## '):
        title = stripped[3:]
        # Remove leading number + period
        m = re.match(r'^\d+\.\s*(.+)$', title)
        if m:
            out.append(f'\\section{{{m.group(1)}}}\n\n')
        elif title in ('引言', '总结'):
            out.append(f'\\section*{{{title}}}\n\n')
        else:
            out.append(f'\\section{{{title}}}\n\n')
        i += 1
        continue

    # Top-level heading (skip, handled by template)
    if stripped.startswith('# ') and not in_math:
        i += 1
        continue

    # Horizontal rule → skip
    if stripped == '---':
        i += 1
        continue

    # Blockquote
    if stripped.startswith('> '):
        quote_text = stripped[2:]
        # Bold
        quote_text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', quote_text)
        out.append(f'\\begin{{quote}}\n{quote_text}\n\\end{{quote}}\n\n')
        i += 1
        continue

    # Bold
    line = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', line)

    # Fix inline $...$ with set notation
    # {f_n} in inline math
    line = re.sub(r'\$\{(f_n)\}\$', r'$\\{\1\\}$', line)
    line = re.sub(r'\$\{([^}]*)\}\$', lambda m:
        '$\\{' + m.group(1) + '\\}$' if '|' in m.group(1) or '>' in m.group(1)
        else m.group(0), line)

    out.append(line)
    i += 1

# Build full LaTeX document
preamble = r"""\documentclass[11pt]{article}

\usepackage{CJKutf8}
\usepackage{math_article}
\usepackage{series_ra}

\renewcommand{\ArticleNumeral}{Sup}
\renewcommand{\ArticleTitle}{一致可积性与 $L^1$ 收敛}
\renewcommand{\ArticleAuthor}{Anqiao Ouyang}
\renewcommand{\ArticleDate}{August 2026}

\begin{document}
\begin{CJK*}{UTF8}{gbsn}

\maketitle

"""

postamble = r"""
\end{CJK*}
\end{document}
"""

body = ''.join(out)

with open('02-uniform-integrability/Sup_zh.tex', 'w') as f:
    f.write(preamble + body + postamble)

print("Done! Written to 02-uniform-integrability/Sup_zh.tex")
