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
    
  def genRoom(self, attempts): # outputs 2 arrays, one of dimensions and one of location
    output = []
    for i in range(attempts):
      room_x = random.randint(1, self.x -1)
      room_y = random.randint(1, self.y -1)
      
      room_length = random.randint(4, 12)
      room_width = random.randint(4, 12)
      
      for x in range(room_length - room_length):
        for y in range(room_width - room_width):
          if self.level[room_x + x][room_y + y] == 1:
            break
      
      for x in range(room_length):
        for y in range(room_width):
          self.level[room_x + x][room_y + y] = 1
