import generatorNew
import recursiveMazeNew

Test = generatorNew.Level("Test", 115, 75)

Test.placeRooms(15)

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

"""
stack = []
stack.append([20,20])
Test.set(20,20,1)

while True:
  if len(stack) > 0:
    Test, stack = recursiveMaze.recurse(Test, stack)
  else:
    break
print printLevel(Test)
"""

Gen = recursiveMazeNew.MazeGen(Test)
Gen.genMaze()
print printLevel(Test)
