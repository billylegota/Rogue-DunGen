import generator

Test = generator.Level("Test", 100, 75)
Test.placeRooms(150)

def printLevel(level):
  output = ""
  for y in range(level.y):
    for x in range(level.x):
      if level.level[x][y] == 0:
        output += "#"
      elif level.level[x][y] == 1:
        output += " "
    output += "\n"
  return output
  
print printLevel(Test)
