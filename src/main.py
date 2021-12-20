import random
from consts import *
from maze import Maze

test = Maze(MAZE_WIDTH, MAZE_HEIGHT, 0)
test.display_cells()
test.generate()
print("---------------------------------------------")
test.display_cells()
test.display_maze()