"""Advent of Code: Day 6 - Puzzle 1"""
import os.path
fileParentPath = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(fileParentPath, "data.txt")

f = open(filePath, "r")
lnList = [line.strip() for line in f.readlines()]

def get_unique_answers(response):
  questions = []

  for char in response:
    if char not in questions:
      questions.append(char)

  return len(questions)

sum = 0
currentResponse = ''

for ln in lnList:
  if ln != '':
    currentResponse += ln
  else:
    sum += get_unique_answers(currentResponse)
    currentResponse = ''

sum += get_unique_answers(currentResponse)

print(sum)

f.close()