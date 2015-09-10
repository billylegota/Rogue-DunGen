import random

# Design:
# 1. Generate an array of odd coords for use in the maze generation algorithm.
# 2. Pick a random point in that new array that is valid and push it to the stack.
# 3. Find the valid neighbors to the NSEW and select one of them. Connect the current and the new points.
# 4. Push new point to stack.
# 5. If there are no valid neighbors then pop the stack.
# 6. GOTO 3 unless the stack is empty.
# Print the map
