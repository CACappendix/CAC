DESTINATION_PDFS=../../PDFs-to-print
DESTINATION_PNGS=../../PNGs-to-print

all: PDFs PNGs

PDFs:
	mkdir -p ${DESTINATION_PDFS}
	xelatex "\\def\LINES{}\\def\AFOURPAPER{}\\input{booklets.tex}"
	mv booklets.pdf ${DESTINATION_PDFS}/booklet-a4.pdf
	xelatex "\\def\LINES{}\\def\LETTERPAPER{}\\input{booklets.tex}"
	mv booklets.pdf ${DESTINATION_PDFS}/booklet-letter.pdf
	make clean

PNGs:
	mkdir -p ${DESTINATION_PNGS}
	xelatex "\\def\BLEEDAREA{}\\input{booklets.tex}"
	convert -density 300 -geometry 1392x1092 booklets.pdf ${DESTINATION_PNGS}/booklet%02d.png
	make clean 

clean:
	rm -f *.aux *.log *.pdf
