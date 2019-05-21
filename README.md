Cards Against Cryptography - The Appendices
==========================

This is an extension for [Cards Against Cryptography](https://github.com/CardsAgainstCryptography/CAC/). 

**Appendix A** provides more questions and in particular more answers.

**Appendix B** is a cryptocurrency themed extension.

Basic Rules
-----------

The rules are the same as for the base game. There are some optional rule extension available (see [RULES.md](./RULES.md)) 

License
-------

Cards Against Cryptography - The Appendices is shamelessly based on Cards Against Cryptography, which was released under a Creative Commons BY-NC-SA 2.0 license (https://creativecommons.org/licenses/by-nc-sa/2.0/).

<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/2.0/88x31.png" />

Cards Against Cryptography - The Appendices is released under the same license, which means you can use, remix, and share the game for free, but cannot sell it.

Contributing
------------

Feel free to create your own extension for Cards Against Cryptography; See [PROJECT.md](./PROJECT.md) for more details on the source files.

Building
------------

The top-level Makefile can be used to recompile printable PDF and PNG versions of the cards:

    make PDFs PNGs

This should work on reasonable Linux or macOS systems.  You need to have xelatex, python3, and ImageMagick's convert command in your path.  One of the cards uses the Comic Sans font, so you need to have that on your system as well, possibly by installing the TeXLive packaging `comicsans` or installing it in your operating system's fonts folder.

You can build specific releases of the cards using environment variables, e.g.

    make PDFs PNGs WHITE=white-appendix-a BLACK=black-appendix-a

Printed copies
--------------

Since Cards Against Humanity was released under a BY-NC-SA 2.0 license, the "non-commercial" aspect of that license implies that we cannot sell you a copy of this game.  

You can make your own printed copy in three ways.  

1. **Print at home.**  Under the `PDFs-to-print` folder, there are printable PDFs of all the cards, formatted for 2-sided printing on either A4 or letter paper.  You'll use up all the toner if print pages and pages of all-black backgrounds, so you could use the gray background instead.
2. **Print at a local printshop.** You could also take the PDFs to your local print shop and have them print it on cardstock (80-pound or higher).  Use a paper cutter to cut out the cards.
3. **Print via a commercial custom card manufacturer.**  The original version of Cards Against Cryptography was printed using MakePlayingCards.com.  The folder `PNGs-to-print` contains the PNG images required to print a deck of cards at MakePlayingCards.com's [US Game Deck Size](https://www.makeplayingcards.com/design/custom-us-game-deck-size-cards.html), along with a [bi-fold (4 side) instruction booklet](https://www.makeplayingcards.com/pops/booklet-guide.html). Uploading the images and configure the project takes about 10 minutes.

Version
-------

This is the 1.0 edition of Cards Against Cryptography - The Appendices.
