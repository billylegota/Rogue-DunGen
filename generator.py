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
    
    # Stores the regions (rooms) as an array of rectangles.
    self.regions = []
    
    # Stores the level data as a 2D array or integers
    self.level = []
    for x in range(self.x):
      self.level.append([])
      for y in range(self.y):
        self.level[x].append(0)

  # Hook for getting the value of a cell (Should probably be removed)
  def get(self, x, y):
    return self.level[x][y]

  # Hook for setting the value of a cell (Should probably be removed)
  def set(self, x, y, value):
    self.level[x][y] = value

  # Attempts to place a series of rectangular regions ranging from 4x4 to 12x12 on the map (only even sizes)
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
              
  # Fills the map with mazes.
  def genMaze(self):
    self.stack = []

    while True:
      attempt = [random.choice(range(self.x - 1)[1::2]), random.choice(range(self.y - 1)[1::2])]
      print attempt
      if self.get(attempt[0], attempt[1]) == 0:
        self.set(attempt[0], attempt[1], 1)
        self.stack.append(attempt)
        self.regions.append([attempt, attempt]) # Add the maze start to the regions list.
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
  
  # Combines all of the seperate regions with doors.
  def unify(self, doorChance=0.25): # Chance of there being a second doorway leading into a region.
    pass

  # Places n up and n down stairwells (do not have to correspond w/ the stairwells directly above or below)
  def placeStairs(self, up, down):
    pass

