import os.path
data = [line.strip() for line in open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.txt"), "r").readlines()]
trees, col, row = 0, 0, 0

while row + 1 < len(data):
  col += 3
  row += 1  
  trees += 1 if data[row][col % len(data[row])] == '#' else 0
print(trees)
