# Re-implamentation of the Rogue-DunGen Dungeon generator with more classiness

import random

class Level(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

    self.regions = []
    
    self.data = [[0 for i in range(x)] for i in range(y)]


  def checkPoint(self, x, y):
    if 0 < x < self.x and 0 < x < self.y:
      return True
    return False


  def get(self, x, y):
    if self.checkPoint(x, y):
      return self.data[x][y]


  def set(self, x, y, value):
    if self.checkPoint(x, y):
      self.data[x][y] = value


  # Returns the number of cells DIRECTLY adjacent to the cell that are un-carved
  def sumNeighbors(self, x, y):
    output = 0
    if self.checkPoint(x, y):
      for dir in [[x - 1, y], [x, y - 1], [x, y + 1], [x + 1, y]]:
        if self.checkPoint(dir[0], dir[1]):
          if self.get(dir[0], dir[1]) == 0:
            output += 1
    return output


  # Get the positions of the cells offset by one that are un-carved
  def getValidNeighbors(self, x, y):
    output = []
    if self.checkPoint(x, y):
      for dir in [[x - 2, y], [x, y - 2], [x, y + 2], [x + 2, y]]:
        if self.checkPoint(dir[0], dir[1]):
          if self.get(dir[0], dir[1]) == 0:
            output.append([dir[0], dir[1]])
    return output


  # Check if a rectangular region is occupied
  def checkRect(self, x1, y1, x2, y2):
    if x2 < self.x - 1 and y2 < self.y - 1:
      for x in range(x1 - 1, x2 + 1):
        for y in range(y1 - 1, y2 + 1):
          if self.get(x, y) == 1:
            return False
      return True
    return False


  ###################
  # Room Generation #
  ###################


  # Generate a single random room.
  def genRoom(self, xRange, yRange):
    while True:
      x1 = random.choice(range(1, self.x - 1)[0::2])
      y1 = random.choice(range(1, self.y - 1)[0::2])
      
      x2 = x1 + random.choice(xRange)
      y2 = y1 + random.choice(yRange)
      return x1, y1, x2, y2


  # Place a room that has been checked.
  def placeRoom(self, x1, y1, x2, y2):
    for x in range(x1, x2):
      for y in range(y1, y2):
        self.set(x, y, 1)


  # Attempt to place a room attempts times. (More attempts / area = more dense room placement)/
  def placeRooms(self, attempts):
    # Variance b/w min and max X and Y dimensions
    xRange, yRange = range(5,13)[0::2], range(5, 13)[0::2]
    for i in range(attempts):
      room = self.genRoom(xRange, yRange)
      if self.checkRect(room[0], room[1], room[2], room[3]):
        self.placeRoom(room[0], room[1], room[2], room[3])
        self.regions.append(room)


  ###################
  # Maze Generation #
  ###################
  
  
  # Outline
  # 1. Choose a random point that is at an odd coord and has no carved out neighbours. Add this to the stack.
  # 2. Find any points offset by 2 from the current point that are not carved.
  # 3. Choose any of these points and connect it to the current point then append the new point to the stack.
  # 4. Keep repeating steps 2 - 3 until the stack is empty. If there are no valid neighbours then pop from the stack.
  
  def findValidPoints(self):
    output = []
    for x in range(1, self.x - 1)[0::2]:
      for y in range(1, self.y - 1)[0::2]:
        if self.sumNeighbors(x, y) == 0:
          output.append([x, y])
    return output
