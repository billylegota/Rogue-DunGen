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
    
  def genRoom(self, x_var=range(4,12)[1::2], y_var=range(4,12)[1::2]):
    room_top = [random.choice(range(self.x - 1)[1::2]), random.choice(range(self.y - 1)[1::2])]
    room_bottom = [room_top[0] + random.choice(x_var), room_top[1] + random.choice(y_var)]

    return room_top, room_bottom
    
  def checkRoom(self, room):
    print room
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
