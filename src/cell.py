from consts import *


class Cell():
    def __init__(self, width, height, id, x, y):
        self.width = width
        self.height = height
        self.id = id
        self.walls = WALL_TOP | WALL_RIGHT | WALL_BOTTOM | WALL_LEFT | CELL_NOT_VISITED

    # x = id - (id // width) * width : y = 93 - (93 /10 ) * 10 = 3 X -> COL NUM
        self.x = x
    # y = id // maze_width : x = 9 / 10 = 0  Y-> ROW NUM
        self.y = y
        self.bfs_step_num = "x"

# EoF
