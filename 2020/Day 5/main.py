"""Advent of Code: Day 5 - Puzzles 1 and 2"""
import os.path
fileParentPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(fileParentPath, "data.txt")

f = open(filePath, "r")
lnList = [line.strip() for line in f.readlines()]

maxId = 0
ids = []

for boardingPass in lnList:
  row = int(boardingPass[:7].replace("F", "0").replace("B", "1"), 2)
  col = int(boardingPass[7:].replace("L", "0").replace("R", "1"), 2)
  maxId = max(maxId, row * 8 + col)
  id = row * 8 + col
  ids.append(id)

for id in ids:
  if id + 1 not in ids and id + 2 in ids:
    missingBoardingPass = id + 1    

print(maxId)
print(missingBoardingPass)

f.close()