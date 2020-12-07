"""Advent of Code: Day 7 - Puzzle 1"""
import os.path
fileParentPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(fileParentPath, "data.txt")

f = open(filePath, "r")
lnList = [line.strip() for line in f.readlines()]

def get_num_bags(clr):
  # Get all bags that contain color and is not a parent bag
  lns = [ln for ln in lnList if clr in ln and ln.index(clr) != 0]

  allClrs = []

  if len(lns) == 0:
    return []
  else:
    # Remove colours at start of string
    clrs = [ ln[:ln.index(" bags")] for ln in lns ]

    # Verify that color isn't already in list
    clrs = [ clr for clr in clrs if clr not in allClrs ]

    for clr in clrs:
      allClrs.append(clr)
      bags = get_num_bags(clr)
      allClrs += bags

    # Remove duplicates
    uniqueClrs = []

    for clr in allClrs:
      if clr not in uniqueClrs:
        uniqueClrs.append(clr)

    return uniqueClrs

clrs = get_num_bags("shiny gold")

# Output color count
print(len(clrs))

f.close()