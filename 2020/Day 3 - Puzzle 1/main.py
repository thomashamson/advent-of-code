"""Advent of Code: Day 3 - Puzzle 1"""

import os.path
fileParentPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(fileParentPath, "data.txt")

# Open file
f = open(filePath, "r")

# Collect data and remove all newline characters
lnList = [line.strip() for line in f.readlines()]

# Initialise variables
treeCount = 0
dataCol = 0
dataRow = 0

# Loop through each row of data
while dataRow + 1 < len(lnList):
  dataCol += 3
  dataRow += 1

  # Collect char
  char = lnList[dataRow][dataCol % len(lnList[dataRow])]

  # Add to tree count if char is a tree
  if char == '#':
    treeCount += 1

# Output tree count
print(treeCount)

# Close file
f.close()