"""Advent of Code: Day 8 - Puzzle 2"""
import os.path
fileParentPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(fileParentPath, "data.txt")

f = open(filePath, "r")
lnList = [line.strip() for line in f.readlines()]

def get_acc_eof():
  acc = 0
  ln = 0
  instructions = []

  while ln not in instructions:
    instructions.append(ln)
    currentInstruction = lnList[ln]
    currentInstruction = currentInstruction.split()
    cmd = currentInstruction[0]
    num = int(currentInstruction[1])

    if cmd == 'acc':
      acc += num
      ln += 1
    elif cmd == 'jmp':
      ln += num
    elif cmd == 'nop':
      ln += 1

    if ln >= len(lnList):
      return acc, True

  return acc, False

for ln in range(len(lnList)):
  if 'jmp' in lnList[ln]:
    lnList[ln] = lnList[ln].replace('jmp', 'nop')
    acc, found = get_acc_eof()

    if found:
      print(acc)
      break
    else:
      lnList[ln] = lnList[ln].replace('nop', 'jmp')

f.close()