Project Structure
============================

    .
    ├── src                     # Source files
    ├── PDFs-to-print           # PDFs output directory
    ├── PNGs-to-print           # PNGs output directory
    ├── Makefile
    ├── LICENSE.txt
    ├── PROJECT.md
    ├── README.md
    └── RULES.md


### Source files

The folder `src` contains the source files for the CAC appendices.

    .
    ├── ...
    ├── src                     # Source files
    │   ├── booklet             # sources files for booklets
    │   ├── cards               # sources files for cards
    │   ├── data                # questions and answers
    │   │   ├── black-*.txt     # csv files with questions
    │   │   └── white-*.txt     # csv files with answers
    │   └── common.tex          # common definitions for both cards and booklets
    └── ...
	
#### common.tex

The file `common.tex` contains the latex packages and common macros for booklets and cards.
In particular it defines:

* Fonts, and font size
* Color schemes, e.g. black-on-white or white-on-black
* CAC-icon and icons for the appendices
* Different macros for cards, for example the `\BLANK` macro (see Data --> Entries)

#### Booklet

The folder `src/booklet` contains the source files for the booklets.

    .
    ├── ...
    ├── src                      # Source files
    │   ├── ...
    │   ├── booklet              # sources files for booklets
    │   │   ├── booklet.tex      # defines layout element for booklets
    │   │   ├── booklets.tex     # contains the booklet pages
    │   │   ├── icons            # booklet icons
    │   │   └── Makefile         # makefile
    │   ├── ...
    │   └── common.tex           # .tex file with common definitions for both cards and booklets
    └── ...

#### Cards

The folder `src/cards` contains the source files for the cards.

    .
    ├── ...
    ├── src                      # Source files
    │   ├── ...
    │   ├── cards                # sources files for cards
    │   │   ├── back_single.tex  # template for backs of single PNG cards	
    │   │   ├── black_full.tex   # template for fullpage black PDFs
    │   │   ├── card.tex         # defines the card layout
    │   │   ├── front_single.tex # template for front of single PNG cards	
    │   │   ├── fullpage.py      # script to combine data for fullpage PDFs
    │   │   ├── fullpage.tex     # defines the layout for fullpage PDFs
    │   │   ├── img              # images for special cards
    │   │   ├── Makefile         # makefile
    │   │   ├── single.py        # script to combine data for single PNG cards	
    │   │   └── white_full.tex   # template for fullpage white PDFs
    │   ├── ...
    │   └── common.tex           # .tex file with common definitions for both cards and booklets
    └── ...
	
##### Card Layout

The card layout is defined in `card.tex` which loads `common.tex`.

	
#### Data

##### CSV-files

The csv-files `data/black-*.txt` contain questions while the files
`data/white-*.txt`.
The filenames `data/black.txt` and `data/white.txt` are reserved and will be overwritten by the make process.
In particular, make will combine all files of the form `data/black-*.txt` in `data/black.txt` and all files of the form `data/white-*.txt` in `data/white.txt`.
The files `data/black.txt` and `data/white.txt` are the default choice for card data.

##### Format

The csv-files are formatted as follows.
Each entry consists of three comma-separated values:

    # text, advice, extra logo
    "``A'' as in \BLANK not \BLANK.","\drawN{1}","\appendixA"

Empty lines and lines starting with # (comments) are ignored.

##### Entries

An entry consists of the following values:

* `text`: The card-text, e.g. a question or answer 
* `advice`: Additional information or instructions
* `extralogo`: An additional icon (beside the CACicon) 

Each entry must be surrounded by "" (can be empty) and may contain arbitrary latex code. In particular, the following macros can be used:

* The macro `\BLANK` can be used to add a blank line. The macro takes an optional length argument, e.g. `\BLANK[5ex]` creates a blank line of length `5ex`.
* The macro `\CENSOR` can be used to create a censored word block. The macro takes an optional length argument, e.g. `\CENSOR[5ex]` creates a block of length `5ex`.
* The macro `\circled` takes some text, e.g. a number, as input and creates a circle around that text.
* The macro `\circlef` takes some text, e.g. a number, as input and creates a filled circle around that text.
* The macro `\drawN` takes some text, e.g. a number n, as input and creates PICK n text.
* The macro `\appendixA` creates the Appendix A logo.
* The macro `\appendixB` creates the Appendix B logo.

Building
============================

The top-level Makefile can be used to recompile printable PDF and PNG versions of the cards:

    make PDFs PNGs
	
You can build specific releases of the cards using environment variables, e.g.

    make PDFs PNGs WHITE=white-appendix-a BLACK=black-appendix-a
	
To create square png-cards use the Makefile in `src/cards`:

    make sqPNGs