.DEFAULT_GOAL := all


.PHONY: all
all: pdf html clean


.PHONY: pdf
pdf:
	@mkdir -p ../target
	@latexmk -quiet -pdf bmkg.tex; \
	  mv bmkg.pdf ../target;


.PHONY: html
html:
	@mkdir -p ../target
	@python extract.py
	@cp sorttable.js ../target/sorttable.js


.PHONY: clean
clean:
	@latexmk -C
	@rm -f *.run.xml *.bbl
