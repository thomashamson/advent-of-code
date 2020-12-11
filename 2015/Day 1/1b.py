with open('data', 'r') as file:
  data = file.read()

count = 0
currentChar = 0

for char in data:
  if char == '(':
    count += 1
  elif char == ')':
    count -= 1
  
  if count == -1:
    print(currentChar+1)
    break
  
  currentChar += 1