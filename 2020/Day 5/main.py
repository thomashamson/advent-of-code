"""Advent of Code: Day 5 - Puzzles 1 and 2"""
import os.path
fileParentPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(fileParentPath, "data.txt")

# Open file
f = open(filePath, "r")

# Collect data
lnList = [line.strip() for line in f.readlines()]

maxId = 0
ids = []

# Loop boarding passes
for boardingPass in lnList:

  # Change row to binary
  row = boardingPass[:7].replace("F", "0").replace("B", "1")

  # Convert
  row = int(row, 2)
  
  # Change col to binary
  col = boardingPass[7:].replace("L", "0").replace("R", "1")

  # Convert
  col = int(col, 2)

  # Use current or new max
  maxId = max(maxId, row * 8 + col)

  # ID
  id = row * 8 + col

  # Append ID
  ids.append(id)

# Loop ids
for id in ids:
  if id + 1 not in ids and id + 2 in ids:
    missingBoardingPass = id + 1    

# Output
print(maxId)
print(missingBoardingPass)

# Close file
f.close()