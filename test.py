import generatorFull2
import recursiveMaze

Test = generatorFull2.Level(115, 75)

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
  
print printLevel(Test)

Test.genMaze()

print printLevel(Test)
