import Generator

Test = Generator.Level(85, 25)

Test.genRooms(30)

def printLevel(level):
  output = ""
  for y in range(level.y):
    for x in range(level.x):
      if level.level[x][y] == 0:
        output += "#"
      elif level.level[x][y] == 1:
        output += "."
    output += "\n"
  return output

Test.genMaze()

print printLevel(Test)
