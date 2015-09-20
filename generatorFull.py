import random

"""
Tiles:
------
0 : Stone
1 : Floor
2 : Door
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


  # Maze Generator:
  # 1. Generate an array of odd coords for use in the maze generation algorithm.
  # 2. Pick a random point in that new array that is valid and push it to the stack.
  # 3. Find the valid neighbors to the NSEW and select one of them. Connect the current and the new points.
  # 4. Push new point to stack.
  # 5. If there are no valid neighbors then pop the stack.
  # 6. unless the stack is empty GOTO 3.
  
  def genMaze(self):
    self.stack = []
    
    def getNeighbors(self, x, y):
      output = []
      for dir in [[x - 2, y], [x, y - 2], [x, y + 2], [x + 2, y]]:
        try:
          result = self.get(dir[0], dir[1])
          if result == 0 and 1 <= dir[0] < self.x - 1 and 1 <= dir[1] < self.y - 1:
            output.append(dir)
        except:
          pass
      return output
    
    def connect(self, p1, p2):
      self.set(p2[0], p2[1], 1)
    
      if p1[0] == p2[0]:
        if p1[1] > p2[1]:
          self.set(p2[0], p2[1] + 1, 1)
        
        elif p1[1] < p2[1]:
          self.set(p2[0], p2[1] - 1, 1)
        
      elif p1[1] == p2[1]:
        if p1[0] > p2[0]:
          self.set(p2[0] + 1, p2[1], 1)
        
        elif p1[0] < p2[0]:
          self.set(p2[0] - 1, p2[1], 1)    
      
    while True:
      attempt = [random.choice(range(self.x - 1)[1::2]), random.choice(range(self.y - 1)[1::2])]
      print attempt
      if self.get(attempt[0], attempt[1]) == 0:
        self.set(attempt[0], attempt[1], 1)
        self.stack.append(attempt)
        break

    while len(self.stack) != 0:
      current = self.stack[len(self.stack) - 1]
      options = getNeighbors(self, current[0], current[1])
    
      if len(options) > 0:
        option = random.choice(options)
        connect(self, current, option)
        self.stack.append(option)
      else:
        self.stack.pop()

