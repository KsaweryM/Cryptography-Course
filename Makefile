# Builds every presentation in Lecture*/ into builded_presentation/<name>.pdf.
# Each lecture has its own Makefile (with the PDF name in NAME); this one calls it and copies the slides.
#
#   make                 build all presentations
#   make 4               build a single presentation by its number
#   make 3 5             build several presentations
#   make rebuild-4       build one presentation from scratch, even if nothing changed
#   make rebuild         build all presentations from scratch
#   make notes           also build the speaker notes (Polish, kept locally, in Lecture*/)
#   make list            show the available lectures
#   make clean-4         remove the auxiliary files and the PDFs of one presentation
#   make clean           remove auxiliary files and PDFs

PDF      := builded_presentation
LECTURES := $(sort $(patsubst %/main.tex,%,$(wildcard Lecture*/main.tex)))

# Lecture number, e.g. Lecture4 -> 4
number = $(patsubst Lecture%,%,$(1))
# PDF name of a lecture, read from its Makefile, e.g. Lecture_4_Diffie-Hellman_and_ElGamal
name   = $(strip $(shell sed -n 's/^NAME *:= *//p' $(1)/Makefile))

NUMBERS := $(foreach l,$(LECTURES),$(call number,$(l)))
PDFS    := $(foreach l,$(LECTURES),$(PDF)/$(call name,$(l)).pdf)

.PHONY: all notes list rebuild clean FORCE $(NUMBERS) $(NUMBERS:%=rebuild-%) $(NUMBERS:%=clean-%)

all: $(PDFS)

# one rule per lecture: the lecture's own Makefile decides what is out of date
define LECTURE_RULES
$(PDF)/$(call name,$(1)).pdf: FORCE
	@$$(MAKE) --no-print-directory -C $(1) slides
	@mkdir -p $(PDF)
	@cmp -s $(1)/$(call name,$(1)).pdf $$@ || { cp $(1)/$(call name,$(1)).pdf $$@ && echo "updated $$@"; }

$(call number,$(1)): $(PDF)/$(call name,$(1)).pdf

clean-$(call number,$(1)):
	$$(MAKE) --no-print-directory -C $(1) clean
	rm -f $(PDF)/$(call name,$(1)).pdf

rebuild-$(call number,$(1)):
	$$(MAKE) --no-print-directory clean-$(call number,$(1))
	$$(MAKE) --no-print-directory $(call number,$(1))
endef
$(foreach l,$(LECTURES),$(eval $(call LECTURE_RULES,$(l))))

FORCE:

notes:
	@$(foreach l,$(LECTURES),{ [ ! -f $(l)/notes.tex ] || $(MAKE) --no-print-directory -C $(l) notes; } &&) true

rebuild:
	$(MAKE) clean
	$(MAKE) all

list:
	@$(foreach l,$(LECTURES),echo "  make $(call number,$(l))    $(call name,$(l))";)

clean:
	@$(foreach l,$(LECTURES),$(MAKE) --no-print-directory -C $(l) clean &&) true
	rm -rf $(PDF)
