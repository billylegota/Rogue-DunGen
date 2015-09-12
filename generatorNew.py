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
    
    self.regions = []
    self.level = self.genLevel()
    
  def genLevel(self):
    output = []
    for x in range(self.x):
      output.append([])
      for y in range(self.y):
        output[x].append(0)
        
    return output
    
  def get(self, x, y):
    return self.level[x][y]
    
  def set(self, x, y, value):
    self.level[x][y] = value
    
  def genRoom(self, x_var=[4,12], y_var=[4,12]):
    room_top = [random.randint(1, self.x -1), random.randint(1, self.y -1)]
    room_bottom = [random.randint(room_top[0] + x_var[0], room_top[0] + x_var[1]), random.randint(room_top[1] + y_var[0], room_top[1] + y_var[1])]
    
    return room_top, room_bottom
    
  def checkRoom(self, room):
    x1, y1 = room[0]
    x2, y2 = room[1]

    if x1 > self.x -1 or x2 > self.x -1 or y1 > self.y -1 or y2 > self.y -1:
        return False
    
    for x in range(x1 -1, x2 + 1):
      for y in range(y1 -1, y2 + 1):
        if self.level[x][y] == 1:
          return False
          
    return True
    
  def placeRooms(self, attempts):
    for i in range(attempts):
      room = self.genRoom()
      if self.checkRoom(room):
        self.regions.append(room)
        
        x1, y1 = room[0]
        x2, y2 = room[1]
        
        for x in range(x1, x2):
          for y in range(y1, y2):
            self.level[x][y] = 1
