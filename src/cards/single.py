#!/usr/local/bin/python3
import os
import csv

black_prefix = os.environ["BLACK"] if "BLACK" in os.environ else "black"
white_prefix = os.environ["WHITE"] if "WHITE" in os.environ else "white"
questions = "../data/" + black_prefix + ".txt"
answers = "../data/" + white_prefix + ".txt"
frontdata = "front.data"
backdata = "back.data"

frontcard = "\\begin{cardpage}\\cardfront{0}{0}{%s}{%s}{%s}\\end{cardpage}"
backcard = "\\begin{cardpage}\\cardback{0}{0}\\end{cardpage}"
newpage = "\\newpage"
colorchange = "\\whitecardtrue\\setcolorscheme"

#Open data files
with open(frontdata, 'w') as front:
    with open(backdata, 'w') as back:
        print("Reading " + questions)
        it = 0
        with open(questions) as csv_file:
            source = csv.reader((line for line in csv_file if not line.startswith('#') and not line.isspace()),delimiter=',')
            for line in source:
                if len(line) < 3:
                    continue
                line[2] = line[2].split('#')[0]
                if it > 0:
                    print(newpage, file=front)
                    print(newpage, file=back)
                print(frontcard % (line[0],line[1],line[2]), file=front)
                print(backcard, file=back)
                it += 1
        print("Switching colours")
        if it > 0:
            print(newpage,file=front)
            print(newpage,file=back)
        print(colorchange, file=front)
        print(colorchange, file=back)
        print("Reading " + answers)
        it = 0
        with open(answers) as csv_file:
            source = csv.reader((line for line in csv_file if not line.startswith('#') and not line.isspace()),delimiter=',')
            for line in source:
                if len(line) < 3:
                    continue
                line[2] = line[2].split('#')[0]
                if it > 0:
                    print(newpage, file=front)
                    print(newpage, file=back)
                print(frontcard % (line[0],line[1],line[2]), file=front)
                print(backcard, file=back)
                it += 1