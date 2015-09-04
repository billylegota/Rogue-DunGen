import random

# What we need to do:
# 1. Be able to tell wether a tile is ok for corridor forming.
# 2. Be able to choose a random tile that is ok and recurse from that point

def genMaze(level, x, y):
  level = level.level
  stack = []
  
  dirs = {"N": [0, -1], "S": [0, 1], "E": [1, 0], "W": [-1, 0]}
  
  def checkPoint(x, y):
    neighbors = 0
    for dir in dirs.keys():
      neighbors += level[dirs[dir][0]][dirs[dir][1]] # Add the value of the North, South, East and Western tiles...
    if neighbors == 1:
      return True
    return False
      
