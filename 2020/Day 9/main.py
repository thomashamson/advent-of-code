"""Advent of Code: Day 9 - Puzzles 1 and 2"""
import os.path
fileParentPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(fileParentPath, "data.txt")

f = open(filePath, "r")
lnList = [int(line.strip()) for line in f.readlines()]

# 2089807806

def get_bad_number():
  # Get preamble
  preamble = lnList[0:25]

  # Loop rest of numbers
  for ln in lnList[26:len(lnList)]:
    foundBadNumber = False
    for p in preamble:
      # If calc in preamble
        if ln - p in preamble:
            foundBadNumber = True
        if foundBadNumber:
            preamble.pop(0)
            preamble.append(ln)
            break
    if not foundBadNumber:
        return ln

def findEncryptionWeakness(badNumber):
    contiguousSet = []
    for ln in lnList:
        if sum(contiguousSet) < badNumber:
            contiguousSet.append(ln)
            continue
        else:
            while True:
                if sum(contiguousSet) > badNumber:
                    contiguousSet.pop(0)
                else:
                    break
            if sum(contiguousSet) == badNumber and len(contiguousSet) >= 2:
                contiguousSet.sort()
                return contiguousSet[0] + contiguousSet[-1]
            contiguousSet.append(ln)

print(get_bad_number())
print(findEncryptionWeakness(get_bad_number()))

f.close()