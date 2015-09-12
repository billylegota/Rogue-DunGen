import random

# Design:
# 1. Generate an array of odd coords for use in the maze generation algorithm.
# 2. Pick a random point in that new array that is valid and push it to the stack.
# 3. Find the valid neighbors to the NSEW and select one of them. Connect the current and the new points.
# 4. Push new point to stack.
# 5. If there are no valid neighbors then pop the stack.
# 6. GOTO 3 unless the stack is empty.
# Print the map

class MazeGen(object):
  def __init__(self, level):
    self.level = level
    self.stack = []
    
  def getNeighbors(self, x, y):
    output = []
    for dir in [[x - 2, y], [x, y - 2], [x, y + 2], [x + 2, y]]:
      try:
        result = self.level.get(dir[0], dir[1])
        if result == 0:
          output.append(dir)
      except:
        pass
    return output
    
  def connect(self, p1, p2):
    level.set(p2[0], p2[1], 1)
    
    if p1[0] == p2[0]:
      if p1[0] > p2[0]:
        self.level.set(p2[0] + 1, p2[1], 1)
        
      elif p1[0] < p2[0]:
        self.level.set(p2[0] - 1, p2[1], 1)
        
    elif p1[1] == p2[1]:
      if p1[1] > p2[1]:
        self.level.set(p2[0], p2[1] + 1, 1)
        
      elif p1[1] < p2[1]:
        self.level.set(p2[0], p2[1] - 1, 1)
    
    else:
      raise IndexError
      
  def iterate(self):
    current = self.stack[len(self.stack) - 1]
    options = self.getNeighbors(current[0], current[1])
    
    if len(options) > 0:
      option = random.choice(options)
      self.connect(current, option)
      self.stack.append(option)
    else:
      self.stack.pop()
      
  def genMaze(self):
    while True:
      attempt = [random.choice(range(self.level.x - 1)[1::2]), random.choice(range(self.level.y - 1)[1::2])]
      print attempt
      if self.level.get(attempt[0], attempt[1]) == 0:
        self.level.set(attempt[0], attempt[1], 1)
        self.stack.append(attempt)
        break
    
