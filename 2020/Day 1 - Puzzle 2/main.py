"""Advent of Code: Day 1 - Puzzle 2"""

import os.path
fileParentPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(fileParentPath, "data.txt")

# Open file
f = open(filePath, "r")

# Initialize line list
lnList = []

# Populate list
for ln in f:
    # Remove line break
    stripped_line = ln.strip()

    # Append number
    lnList.append(stripped_line)

# Loop and output
for primaryLn in lnList:
    for secondaryLn in lnList:
        if primaryLn != secondaryLn:
            for tertiaryln in lnList:
                if secondaryLn != tertiaryln:
                    lnSum = int(primaryLn) + int(secondaryLn) + int(tertiaryln)
                    if lnSum == 2020:
                        print(
                            primaryLn + ' + ' +
                            secondaryLn + ' + ' +
                            tertiaryln + ' = ' +
                            str(lnSum)
                        )
                        print(
                            primaryLn + ' * ' +
                            secondaryLn + ' * ' +
                            tertiaryln + ' = ' +
                            str(int(primaryLn) *
                                int(secondaryLn) *
                                int(tertiaryln)
                                )
                        )
                        exit()

# Close file
f.close()
