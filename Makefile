export TEXINPUTS=../tex//:

all: thesis.pdf

# LaTeX must be run multiple times to get references right
thesis.pdf: thesis.tex $(wildcard chapters/*.tex) bibliography.bib thesis.xmpdata
	xelatex $<
	bibtex thesis
	xelatex $<
	xelatex $<

clean:
	rm -f tmp/*
	rm -f *.log *.dvi *.aux *.toc *.lof *.lot *.out *.bbl *.blg *.xmpi *.ilg *.idx *.fls *.fdb_latexmk *.xdv
	rm -f thesis.pdf
