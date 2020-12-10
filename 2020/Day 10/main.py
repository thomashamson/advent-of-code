"""Advent of Code: Day 10 - Puzzles 1 and 2"""
import os.path
fileParentPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(fileParentPath, "data.txt")

f = open(filePath, "r")
lnList = [int(line.strip()) for line in f.readlines()]

# Add 0 to list
lnList.append(0)

# Add max plus 3 to list
lnList.append(max(lnList) + 3)

# Sort list smallest to largest
lnList.sort()

diffs = [0] * 4

# Loop
for ln in range(1, len(lnList)):
  adjDiff = lnList[ln] - lnList[ln-1]
  diffs[adjDiff] += 1

# Output
print(diffs[1] * diffs[3])

paths = [0] * (max(lnList) + 1)
paths[0] = 1

# Loop
for ln in range(1, max(lnList) + 1):
  for x in range(1, 4):
    if (ln - x) in lnList:
      paths[ln] += paths[ln-x]

# Output
print(paths[-1])

f.close()