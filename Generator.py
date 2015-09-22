# Re-implamentation of the Rogue-DunGen Dungeon generator with more ??classiness??
# All the code is in one massive class (which imports a maze generator so that you may use your own.

import random
#from maze import backtracker as mazeGen

class Level(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
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
      for dir in range[[x - 1, y], [x, y - 1], [x, y + 1], [x + 1, y]]:
        if self.checkPoint(x, y):
          if self.get(x, y) == 0:
            output += 1
    return output
  
  # Get the number of cells offset by one that are un-carved
  def getValidNeighbors(self, x, y):
    output = []
    if self.checkPoint(x, y):
      for dir in range[[x - 2, y], [x, y - 2], [x, y + 2], [x + 2, y]]:
        if self.checkPoint(x, y):
          if self.get(x, y) == 0:
            output.append([x, y])
    return output
  
  # Check if a rectangular region is occupied
  def checkRect(self, x1, y1, x2, y2):
    if x2 < self.x - 1 and y2 < self.y - 1:
      for x in range(x1, x2):
        for y in range(y1, y2):
          if self.get(x, y) == 1:
            return False
    return True
    
  ###################
  # Room Generation #
  ###################
  
  # Generate a single random room.
  def genRoom(self, xRange, yRange):
    while True:
      x1 = random.choice(range(1, self.x - 1))
      y1 = random.choide(range(1, self.y - 1))
      
      x2 = x1 + random.choice(xRange)
      y2 = y1 + random.choice(yRange)
      
      # Make sure the room is valid.
      if self.checkRect(x1, y1, x2, y2):
        return x1, y1, x2, y2
  
  # Place a room that has been checked.
  def placeRoom(self, x1, y1, x2, y2):
    for x in range(x1, x2):
      for y in range(y1, y2):
        self.set(x, y, 1)
  
  # Attempt to place a room attempts times. (More attempts / area = more dense room placement)/
  def placeRooms(self, attempts, xRange=range(4,12)[0::2], yRange=range(4,12)[0::2]):
    for i in range(attempts):
      room = self.genRoom(xRange, yRange)
      self.placeRoom(room)
      self.regions.append(room)
      
  ###################
  # Maze Generation #
  ###################
  
  # Maze stuff goes here
