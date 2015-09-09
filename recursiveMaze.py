import random

# What we need to do:
# 1. Be able to tell wether a tile is ok for corridor forming.
# 2. Be able to choose a random tile that is ok and recurse from that point

"""
def genMaze(level, x, y):
  level = level.level
  stack = []
  
  dirs = {"N": [0, -1], "S": [0, 1], "E": [1, 0], "W": [-1, 0]}
  
  def checkPoint(x, y):
    neighbors = 0
    for dir in dirs.keys():
      neighbors += level[dirs[dir][0] + x][dirs[dir][1] + y] # Add the value of the North, South, East and Western tiles...
    if neighbors == 1:
      return True
    return False
    
  def checkNeighbors(x, y):
    neighbors = []
    for dir in dirs.keys():
      if checkPoint(dirs[dir][0] + x, dirs[dir][1] + y):
        neighbors.append([dirs[dir][0] + x, dirs[dir][1] + y])
    return neighbors
"""

def checkTile(level, x, y):
  if 0 < x < len(level.length) - 1 and 0 < y < len(level.with) - 1:
    if level.get(x, y) == 0:
      sum = 0
      for direction in [[x - 1, y], [x, y - 1], [x, y + 1], [x + 1, y]]:
        sum += level.get(direction[0], direction[1])
      if sum == 1:
        return True
  return False
  

def getNeighbors(leve, x, y):
  output = []
  for direction in [[x - 1, y], [x, y - 1], [x, y + 1], [x + 1, y]]:
    if checkTile(level, direction[0], direction[1]):
      output.append(direction)
  return output
  
def recurse(level, stack):
  current = stack[len(stack) - 1]
  choices = getNeighbors(level, current[0], current[1])
  if len choices > 0:
    choice = random.choice(choices)
    stack.append(choice)
    level.set(choices[0], choices[1], 1)
  else:
    stack.pop()
    
