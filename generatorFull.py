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
    self.level = self.genLevel()
    
  def genLevel(self):
    output = []
    for x in range(self.x):
      output.append([])
      for y in range(self.y):
        output[x].append(0)
        
    return output
    
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
            
# Design:
# 1. Generate an array of odd coords for use in the maze generation algorithm.
# 2. Pick a random point in that new array that is valid and push it to the stack.
# 3. Find the valid neighbors to the NSEW and select one of them. Connect the current and the new points.
# 4. Push new point to stack.
# 5. If there are no valid neighbors then pop the stack.
# 6. GOTO 3 unless the stack is empty.
# Print the map

  def genMaze(self):
    def getNeighbors(x, y):
      output = []
      for dir in [[x - 2, y], [x, y - 2], [x, y + 2], [x + 2, y]]:
        try:
          result = self.level.get(dir[0], dir[1])
          if result == 0 and 1 <= dir[0] < self.level.x - 1 and 1 <= dir[1] < self.level.y - 1:
            output.append(dir)
        except:
          pass
      return output
    
    def connect(p1, p2):
      self.level.set(p2[0], p2[1], 1)
    
      if p1[0] == p2[0]:
        if p1[1] > p2[1]:
          self.level.set(p2[0], p2[1] + 1, 1)
        
        elif p1[1] < p2[1]:
          self.level.set(p2[0], p2[1] - 1, 1)
        
      elif p1[1] == p2[1]:
        if p1[0] > p2[0]:
          self.level.set(p2[0] + 1, p2[1], 1)
        
        elif p1[0] < p2[0]:
          self.level.set(p2[0] - 1, p2[1], 1)
    
      else:
        raise IndexError
      
    def iterate():
      current = self.stack[len(self.stack) - 1]
      options = self.getNeighbors(current[0], current[1])
    
      if len(options) > 0:
        option = random.choice(options)
        self.connect(current, option)
        self.stack.append(option)
      else:
        self.stack.pop()
      
    def genMaze():
      while True:
        attempt = [random.choice(range(self.level.x - 1)[1::2]), random.choice(range(self.level.y - 1)[1::2])]
        print attempt
        if self.level.get(attempt[0], attempt[1]) == 0:
          self.level.set(attempt[0], attempt[1], 1)
          self.stack.append(attempt)
          break

      while len(self.stack) != 0:
        iterate()
