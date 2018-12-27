export TEXINPUTS=../tex//:

all: thesis.pdf

# LaTeX must be run multiple times to get references right
thesis.pdf: thesis.tex $(wildcard *.tex) bibliography.bib thesis.xmpdata
	pdflatex -aux-directory=tmp/ -output-directory=tmp/ $<
	cp bibliography.bib tmp
	(cd tmp; bibtex thesis)
	pdflatex -aux-directory=tmp/ -output-directory=tmp/ $<
	pdflatex -aux-directory=tmp/ -output-directory=tmp/ $<
	cp tmp/thesis.pdf .

clean:
	rm -f tmp/*
	rm -f *.log *.dvi *.aux *.toc *.lof *.lot *.out *.bbl *.blg *.xmpi
	rm -f thesis.pdf
