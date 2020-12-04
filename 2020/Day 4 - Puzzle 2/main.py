"""Advent of Code: Day 4 - Puzzle 2"""
import os.path
fileParentPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(fileParentPath, "data.txt")

# Valid fields
validFields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

validPassports = []

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

# Loop
currentPassport = ''
for ln in lnList:
  if ln != '':
    currentPassport += ' ' + ln
  else:
    if is_passport_valid(currentPassport):
      validPassports.append(currentPassport)
    currentPassport = ''

# Check passport at end of data
if is_passport_valid(currentPassport):
  validPassports.append(currentPassport)

# Check byr
def is_passport_data_byr_valid(f):
  f = int(f)
  if f < 1920 or f > 2002:
    return False
  return True

# Check iyr
def is_passport_data_iyr_valid(f):
  f = int(f)
  if f < 2010 or f > 2020:
    return False
  return True

# Check eyr
def is_passport_data_eyr_valid(f):
  f = int(f)
  if f < 2020 or f > 2030:
    return False
  return True

# Check hgt
def is_passport_data_hgt_valid(f):
  units = f[-2:]
  if units not in ['in', 'cm']:
    return False
  f = int(f[:-2])
  if units == 'in':
    if f < 59 or f > 76:
      return False
  elif units == 'cm':
    if f < 150 or f > 193:
      return False
  return True

# Check hcl
def is_passport_data_hcl_valid(f):
  if f[0] != '#':
    return False
  if len(f[1:]) != 6:
    return False
  return True

# Check ecl
def is_passport_data_ecl_valid(f):
  clrs = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  if f not in clrs:
    return False
  return True

# Check pid
def is_passport_data_pid_valid(f):
  if len(f) != 9:
    return False
  return True

# Check if passport data is valid
def is_passport_data_valid(passport):
  passport = passport.split()
  data = {}

  for f in passport:
    key = f[:3]
    value = f[4:]
    data[key] = value

  if not is_passport_data_byr_valid(data['byr']):
    return False

  if not is_passport_data_iyr_valid(data['iyr']):
    return False
    
  if not is_passport_data_eyr_valid(data['eyr']):
    return False

  if not is_passport_data_hgt_valid(data['hgt']):
    return False

  if not is_passport_data_hcl_valid(data['hcl']):
    return False

  if not is_passport_data_ecl_valid(data['ecl']):
    return False

  if not is_passport_data_pid_valid(data['pid']):
    return False

  return True

# Valid count
validCount = 0

# Loop
for passport in validPassports:
  if is_passport_data_valid(passport):
    validCount += 1

# Output valid count
print(validCount)

# Close file
f.close()