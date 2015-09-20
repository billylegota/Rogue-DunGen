import random

"""
Tiles:
------
0 : Stone
1 : Floor
2 : Door
4 : Down stairwell
5 : Up stairwell
"""

class Level(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
    self.regions = []
    
    self.level = []
    for x in range(self.x):
      self.level.append([])
      for y in range(self.y):
        self.level[x].append(0)

  def get(self, x, y):
    return self.level[x][y]

  
  def set(self, x, y, value):
    self.level[x][y] = value


  def genRooms(self, attempts):
    for i in range(attempts):
      x1 = random.choice(range(1, self.x - 1)[0::2])
      y1 = random.choice(range(1, self.y - 1)[0::2])

      x2 = x1 + random.choice(range(4, 12)[1::2])
      y2 = y1 + random.choice(range(4, 12)[1::2])

      if x2 < self.x - 1 and y2 < self.y - 1:
        valid = True
        for x in range(x1 -1, x2 + 1):
          for y in range(y1 -1, y2 + 1):
            if self.level[x][y] == 1:
              valid = False
      
        if valid:
          self.regions.append([[x1, y1], [x2, y2]])
          for x in range(x1, x2):
            for y in range(y1, y2):
              self.level[x][y] = 1
              
  
  def genMaze(self):
    self.stack = []

    while True:
      attempt = [random.choice(range(self.x - 1)[1::2]), random.choice(range(self.y - 1)[1::2])]
      print attempt
      if self.get(attempt[0], attempt[1]) == 0:
        self.set(attempt[0], attempt[1], 1)
        self.stack.append(attempt)
        break

    while len(self.stack) != 0:
      x1, y1 = self.stack[len(self.stack) - 1]

      options = []
      for dir in [[x1 - 2, y1], [x1, y1 - 2], [x1, y1 + 2], [x1 + 2, y1]]:
        try:
          result = self.get(dir[0], dir[1])
          if result == 0 and 1 <= dir[0] < self.x - 1 and 1 <= dir[1] < self.y - 1:
            options.append(dir)
        except:
          pass

      if len(options) > 0:
        x2, y2 = random.choice(options)
        self.set(x2, y2, 1)
        self.stack.append([x2, y2])
    
        if x1 == x2:
          if y1 > y2:
            self.set(x2, y2 + 1, 1)
        
          elif y1 < y2:
            self.set(x2, y2 - 1, 1)
        
        elif y1 == y2:
          if x1 > x2:
            self.set(x2 + 1, y2, 1)
        
          elif x1 < x2:
            self.set(x2 - 1, y2, 1)
      else:
        self.stack.pop()

  def unify(self):
    pass # This is where the region unification code will go

  def placeStairs(self, number):
    pass # This is where the stairwells will be placed

