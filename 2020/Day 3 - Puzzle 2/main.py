"""Advent of Code: Day 3 - Puzzle 2"""

import os.path
fileParentPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(fileParentPath, "data.txt")

# Open file
f = open(filePath, "r")

# Collect data and remove all newline characters
lnList = [line.strip() for line in f.readlines()]

# Create slopes
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total = 1

# Loop through slopes
for slope in slopes:
  treeCount = 0
  dataCol = 0
  dataRow = 0

  # Loop through each row of data
  while dataRow + 1 < len(lnList):
    dataCol += slope[0]
    dataRow += slope[1]

    # Collect char
    char = lnList[dataRow][dataCol % len(lnList[dataRow])]

    # Add to tree count if char is a tree
    if char == '#':
      treeCount += 1

  # Multiply total by tree count
  total *= treeCount

# Output total
print(total)

# Close file
f.close()