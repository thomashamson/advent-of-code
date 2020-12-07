"""Advent of Code: Day 7 - Puzzle 2"""
import os.path
fileParentPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(fileParentPath, "data.txt")

f = open(filePath, "r")
lnList = [line.strip() for line in f.readlines()]

def get_bag_count(clr):
  paramClr = clr
  rule = ''

  for ln in lnList:
    # Get all bags that contain color and is a parent bag
    if ln[:ln.index(" bags")] == clr:
      rule = ln

  # If no bags, it's just the parent bag so return 1
  if 'no' in rule:
    return 1

  # Get bag contents and split
  rule = rule[rule.index('contain')+8:].split()

  counter = 0
  total = 0
  while counter < len(rule):
    count = int(rule[counter])
    clr = rule[counter+1] + ' ' + rule[counter+2]

    total += count * get_bag_count(clr)

    counter += 4

  # Shiny gold case
  if paramClr == 'shiny gold':
    return total
  else:
    return total + 1

bagCount = get_bag_count('shiny gold')

# Output bag count
print(bagCount)

f.close()