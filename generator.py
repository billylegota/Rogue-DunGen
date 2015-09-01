import random

"""
Tiles:
------
0 : Stone
1 : Floor
"""

class Level(object):
  def __init__(self, name, x, y):
    self.name = name
    self.x = x
    self.y = y
    
    self.level = self.genLevel()
    
  def genLevel(self):
    output = []
    for x in range(self.x):
      output.append([])
      for y in range(self.y):
        output[x].append(0)
        
    return output
    
  def genRoom(self): # outputs 2 arrays, one of dimensions and one of location
    output = []
    
    
