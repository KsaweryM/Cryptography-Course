# Post-processing of an SVG made by pdftocairo:
#   - the size in px = the size in pt (pdftocairo writes pt as px, so the figure would look too small),
#   - a white rectangle behind everything (readable in a dark theme),
#   - numbers rounded to 2 decimals (a smaller file).
# Usage: python3 post.py figure.svg
import re
import sys

path = sys.argv[1]
with open(path) as f:
    svg = f.read()

svg = re.sub(r"\d+\.\d{3,}", lambda m: f"{float(m.group(0)):.2f}".rstrip("0").rstrip("."), svg)

head = re.search(r'<svg [^>]*width="([\d.]+)" height="([\d.]+)"[^>]*>', svg)
w = float(head.group(1))
h = float(head.group(2))
tag = head.group(0)
new_tag = tag.replace(f'width="{head.group(1)}"', f'width="{w * 4 / 3:.0f}"', 1)
new_tag = new_tag.replace(f'height="{head.group(2)}"', f'height="{h * 4 / 3:.0f}"', 1)
new_tag += '\n<rect x="0" y="0" width="100%" height="100%" fill="#ffffff"/>'
svg = svg.replace(tag, new_tag, 1)

with open(path, "w") as f:
    f.write(svg)
