#!/usr/local/bin/python3
import os
import csv

black_prefix = os.environ["BLACK"] if "BLACK" in os.environ else "black"
white_prefix = os.environ["WHITE"] if "WHITE" in os.environ else "white"
black_txt = "../data/" + black_prefix + ".txt"
white_txt = "../data/" + white_prefix + ".txt"
sources = [black_txt, white_txt]
destinations = ["black.data", "white.data"]

preamble = "\\begin{cardpage}"
pattern = "\\cardfront{%d * \CARDWIDTH}{%d * \CARDHEIGHT}{%s}{%s}{%s}"
postamble = "\\end{cardpage} \\newpage \\backgroundpage"

for i in range(len(sources)):
    print("Generating " + destinations[i])
    with open(destinations[i], 'w') as destination:
        with open(sources[i]) as csv_file:
            source = csv.reader((line for line in csv_file if not line.startswith('#') and not line.isspace()),delimiter=',')
            it = 0
            for line in source:
                if len(line) < 3:
                    continue
                line[2] = line[2].split('#')[0]
                if (it % 9) == 0:
                    if it > 0:
                        print(postamble, file=destination)
                        print("\\newpage", file=destination)
                    print(preamble, file=destination)
                col = (it % 3)
                row = (it // 3) % 3
                print(pattern % (col, row, line[0],line[1],line[2]), file=destination)
                it += 1
            while (it % 9) != 0:
                col = (it % 3)
                row = (it // 3) % 3
                print(pattern % (col, row, "","",""), file=destination)
                it += 1
            print(postamble, file=destination)