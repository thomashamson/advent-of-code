"""Advent of Code: Day 4 - Puzzle 1"""
import os.path
fileParentPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(fileParentPath, "data.txt")

# Valid fields
validFields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

# Check is passport is valid
def is_passport_valid(passport):
  for vF in validFields:
    if vF not in passport:
      return False
  return True

# Open file
f = open(filePath, "r")

# Collect data
lnList = [line.strip() for line in f.readlines()]

# Valid count
validCount = 0

# Loop
currentPassport = ''
for ln in lnList:
  if ln != '':
    currentPassport += ' ' + ln
  else:
    if is_passport_valid(currentPassport):
      validCount += 1
    currentPassport = ''

# Check passport at end of data
if is_passport_valid(currentPassport):
  validCount += 1

# Output valid count
print(validCount)

# Close file
f.close()