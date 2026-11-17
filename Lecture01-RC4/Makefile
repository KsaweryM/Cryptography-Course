# Builds Lecture 1 (Stream Ciphers and RC4).
#
#   make           build the slides
#   make slides    the same
#   make check     count Overfull warnings and look for en and em dashes in the text
#   make rebuild   build everything from scratch
#   make clean     remove build/ and the PDFs
#
# Auxiliary files go to build/; the PDFs are copied next to this Makefile.

LATEXMK   := latexmk
LATEXOPTS := -pdf -interaction=nonstopmode -halt-on-error -file-line-error

NAME   := Lecture_1_Stream_Ciphers_and_RC4
SLIDES := $(NAME).pdf
BUILD  := build

.PHONY: all slides check rebuild clean

all: $(SLIDES)

slides: $(SLIDES)

$(SLIDES): main.tex
	$(LATEXMK) $(LATEXOPTS) -outdir=$(BUILD)/slides main.tex
	cp $(BUILD)/slides/main.pdf $@

check: all
	@echo "Overfull in the slides: $$(grep -c Overfull $(BUILD)/slides/main.log)"
	@echo "Dashes in the text (should be none):"
	@grep -nP '–|—|(?<![-(\w])--(?![-\w(])|---' main.tex | grep -vP '^\d+:\s*%|\)\s*--\s*\(|--\s*\+\+|\(\w*\)\s*--' || true

rebuild:
	$(MAKE) clean
	$(MAKE) all

clean:
	rm -rf $(BUILD) $(SLIDES)
