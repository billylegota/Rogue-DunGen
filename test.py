import generator
import recursiveMaze

Test = generator.Level("Test", 115, 75)

Test.placeRooms(15)

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
  
print printLevel(Test)

Gen = recursiveMaze.MazeGen(Test)
Gen.genMaze()
print printLevel(Test)
