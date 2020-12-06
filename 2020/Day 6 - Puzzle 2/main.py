"""Advent of Code: Day 6 - Puzzle 2"""
import os.path
fileParentPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(fileParentPath, "data.txt")

f = open(filePath, "r")
lnList = [line.strip() for line in f.readlines()]

def get_all_unique_answers(responses):
  questions = []

  for char in responses[0]:
    allLns = True
    
    for ln in responses:
      if char not in ln:
        allLns = False

    if allLns and char not in questions:
      questions.append(char)

  return len(questions)

sum = 0
currentResponse = []

for ln in lnList:
  if ln != '':
    currentResponse.append(ln)
  else:
    sum += get_all_unique_answers(currentResponse)
    currentResponse = []

sum += get_all_unique_answers(currentResponse)

print(sum)

f.close()