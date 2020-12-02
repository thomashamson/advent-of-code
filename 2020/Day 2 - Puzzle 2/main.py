"""Advent of Code: Day 2 - Puzzle 1"""

import os.path
fileParentPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(fileParentPath, "data.txt")

# Open file
f = open(filePath, "r")

# Initialize line list
lnList = []

# Populate list
for ln in f:
    # Remove line break
    stripped_line = ln.strip()

    # Append string
    lnList.append(stripped_line)

# Initialise valid password count
validPass = 0

# Loop and output
for ln in lnList:
  # Get hyphen char position
  lnHyphen = ln.find('-')

  # Get colon char position
  lnColon = ln.find(':')

  # Get min
  lnMin = int(ln[:lnHyphen])

  # Get max
  lnMax = int(ln[lnHyphen+1:lnColon-2])

  # Get char
  lnChar = ln[lnColon-1:lnColon]

  # Get password
  lnPass = ln[lnColon+2:]

  # Variable to store char count
  lnCount = 0

  for char in lnPass:
      if char == lnChar:
        lnCount = lnCount + 1

  if lnCount >= lnMin and lnCount <= lnMax:
    validPass = validPass + 1

# Output valid password count
print(validPass)

# Close file
f.close()
