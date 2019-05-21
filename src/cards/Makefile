#dirs
DESTINATION_PDFS=../../PDFs-to-print
DESTINATION_PNGS=../../PNGs-to-print/individual-cards
DATASOURCE=../data
#default data
WHITE=white
BLACK=black
	
#Create both PDFs and PNGs
all: PDFs PNGs

#Create fullpage PDFs
PDFs: a4 letter

#Create individual PNGs
PNGs: front.data back.data
	mkdir -p ${DESTINATION_PNGS}
	-rm ${DESTINATION_PNGS}/*.png
	xelatex -interaction=batchmode  -halt-on-error "\\def\BLEEDAREA{}\\input{front_single.tex}"
	convert -density 300 -geometry 732x1101 -strip -scene 1 front_single.pdf ${DESTINATION_PNGS}/FRONT%03d.png
	rm -f front_single.aux front_single.log front_single.pdf
	xelatex -interaction=batchmode  -halt-on-error "\\def\BLEEDAREA{}\\input{back_single.tex}"
	convert -density 300 -geometry 732x1101 -strip -scene 1 back_single.pdf ${DESTINATION_PNGS}/BACK%03d.png
	rm -f back_single.aux back_single.log back_single.pdf
	
#Create square PNGs:
sqPNGs: front.data back.data
	mkdir -p ${DESTINATION_PNGS}
	-rm ${DESTINATION_PNGS}/*.png
	xelatex -interaction=batchmode  -halt-on-error "\\def\BLEEDAREA{}\\def\SQUARECARDS{}\\input{front_single.tex}"
	convert -density 300 -geometry 732x1101 -strip -scene 1 front_single.pdf ${DESTINATION_PNGS}/sqFRONT%03d.png
	rm -f front_single.aux front_single.log front_single.pdf
	xelatex -interaction=batchmode  -halt-on-error "\\def\BLEEDAREA{}\\def\SQUARECARDS{}\\input{back_single.tex}"
	convert -density 300 -geometry 732x1101 -strip -scene 1 back_single.pdf ${DESTINATION_PNGS}/sqBACK%03d.png
	rm -f back_single.aux back_single.log back_single.pdf
	
clean:
	rm -f *.aux *.log *.pdf  *.data *.png
	rm -f ${DATASOURCE}/white.txt
	rm -f ${DATASOURCE}/black.txt	
	
#Create fullpage A4 PDFs
a4:
	mkdir -p ${DESTINATION_PDFS}
	make a4blackblack
	mv black_full.pdf ${DESTINATION_PDFS}/black-a4-black.pdf
	make a4blackgray
	mv black_full.pdf ${DESTINATION_PDFS}/black-a4-gray.pdf
	make a4blackwhite
	mv black_full.pdf ${DESTINATION_PDFS}/black-a4-white.pdf
	make a4whitewhite
	mv white_full.pdf ${DESTINATION_PDFS}/white-a4.pdf
	
#Create fullpage letter PDFs
letter:
	mkdir -p ${DESTINATION_PDFS}
	make letterblackblack
	mv black_full.pdf ${DESTINATION_PDFS}/black-letter-black.pdf
	make letterblackgray
	mv black_full.pdf ${DESTINATION_PDFS}/black-letter-gray.pdf
	make letterblackwhite
	mv black_full.pdf ${DESTINATION_PDFS}/black-letter-white.pdf
	make letterwhitewhite
	mv white_full.pdf ${DESTINATION_PDFS}/white-letter.pdf

#Rules for preparing data
front.data back.data: combine ${DATASOURCE}/*.txt
	WHITE=${WHITE} BLACK=${BLACK} python3 single.py

black.data white.data: combine ${DATASOURCE}/*.txt
	WHITE=${WHITE} BLACK=${BLACK} python3 fullpage.py
	
combine:
	rm -f ${DATASOURCE}/white.txt
	rm -f ${DATASOURCE}/black.txt	
	echo "#DO NOT EDIT AUTO GENERATED\n" | cat - ${DATASOURCE}/white-*.txt > ${DATASOURCE}/white.txt
	echo "#DO NOT EDIT AUTO GENERATED\n" | cat - ${DATASOURCE}/black-*.txt > ${DATASOURCE}/black.txt	

#Rules for compiling the different fullpage templates
a4blackblack: black.data white.data
	xelatex "\\input{black_full.tex}"
	rm -f black_full.aux black_full.log

a4blackgray: black.data white.data
	xelatex "\\def\\BLACKBACKGROUNDGRAY{}\\input{black_full.tex}"
	rm -f black_full.aux black_full.log

a4blackwhite: black.data white.data
	xelatex "\\def\\BLACKBACKGROUNDWHITE{}\\input{black_full.tex}"
	rm -f black_full.aux black_full.log

a4whitewhite: black.data white.data
	xelatex "\\input{white_full.tex}"
	rm -f white_full.aux white_full.log
	
letterblackblack: black.data white.data
	xelatex "\\def\\LETTERPAPER{}\\input{black_full.tex}"
	rm -f black_full.aux black_full.log

letterblackgray: black.data white.data
	xelatex "\\def\\LETTERPAPER{}\\def\\BLACKBACKGROUNDGRAY{}\\input{black_full.tex}"
	rm -f black_full.aux black_full.log

letterblackwhite: black.data white.data
	xelatex "\\def\\LETTERPAPER{}\\def\\BLACKBACKGROUNDWHITE{}\\input{black_full.tex}"
	rm -f black_full.aux black_full.log

letterwhitewhite: black.data white.data
	xelatex "\\def\\LETTERPAPER{}\\input{white_full.tex}"
	rm -f white_full.aux white_full.log