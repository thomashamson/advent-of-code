"""Advent of Code: Day 1 - Puzzle 1"""

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
            lnSum = int(secondaryLn) + int(primaryLn)
            if lnSum == 2020:
                print(secondaryLn + ' + ' + primaryLn + ' = ' + str(lnSum))
                print(
                    secondaryLn + ' * ' +
                    primaryLn + ' = ' +
                    str(int(secondaryLn) * int(primaryLn))
                )
                exit()

# Close file
f.close()
