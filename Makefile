all: clean PDFs PNGs

PDFs:
	cd src/booklet && make PDFs
	cd src/cards && make PDFs

PNGs:
	cd src/booklet && make PNGs
	cd src/cards && make PNGs

clean:
	cd src/booklet && make clean
	cd src/cards && make clean
	cd PDFs-to-print && rm -f *.pdf
	cd PNGs-to-print && rm -f *.png
	cd PNGs-to-print/individual-cards && rm -f *.png
