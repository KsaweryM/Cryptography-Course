#!/bin/sh
# Rebuilds the figures of the Lecture 6 tasks.
#   ./build.sh          all figures
#   ./build.sh 2 3      only task2.tex and task3.tex
# taskN.tex -> build/taskN.pdf (pdflatex) -> ../TaskN/figure.svg (pdftocairo)
# taskNb.tex, if there is one, becomes ../TaskN/figure2.svg.
# A PNG preview of every figure goes to build/ (to look at it, not for git).
set -e
cd "$(dirname "$0")"
mkdir -p build

if [ $# -eq 0 ]; then
  set -- $(ls task*.tex | sed 's/^task\([0-9]*\)b\?\.tex$/\1/' | sort -nu)
fi

for n in "$@"; do
  for f in task$n.tex task${n}b.tex; do
    [ -f "$f" ] || continue
    name=${f%.tex}
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build "$f" > build/$name.out \
      || { tail -30 build/$name.log; exit 1; }
    case $name in
      *b) svg=../Task$n/figure2.svg ;;
      *)  svg=../Task$n/figure.svg ;;
    esac
    pdftocairo -svg build/$name.pdf "$svg"
    python3 post.py "$svg"
    pdftoppm -png -r 96 -singlefile build/$name.pdf build/$name
    echo "$f -> $svg"
  done
done
