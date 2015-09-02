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
    
  def genRoom(self, x_var=12, y_var=12):
    room_top = [random.randint(1, self.x -1), random.randint(1, self.y -1)]
    room_bottom = [random.randint(room_top[0], room_top[0] + x_var), random.randint(room_top[1], room_top[1] + y_var)]
    
    return room_top, room_bottom
    
  def checkRoom(self, room):
    x1, y1 = room[0]
    x2, y2 = room[1]
    
    for x in range(x1, x2):
      for y in range(y1, y2):
        if self.level[x][y] == 1:
          return False
          
    return True
    
  def placeRoom(self, attempts):
    for i in range(attempts):
      room = self.genRoom()
      if self.checkRoom(room):
        
        x1, y1 = room[0]
        x2, y2 = room[1]
        
        for x in range(x1, x2):
          for y in range(y1, y2):
            self.level[x][y] = 1
