from consts import NO_DOOR, D_TOP, D_RIGHT, D_BOTTOM, D_LEFT, W_TOP, W_RIGHT, W_BOTTOM, W_LEFT, CELL_NOT_VISITED


class Cell():
    def __init__(self, size, id, x, y):
        self.size = size  # size for drawing imgs
        self.id = id
        self.walls = W_TOP | W_RIGHT | W_BOTTOM | W_LEFT | CELL_NOT_VISITED
        # x = id - (id // width) * width : y = 93 - (93 /10 ) * 10 = 3 X -> COL NUM
        self.x = x
        # y = id // maze_width : x = 9 / 10 = 0  Y-> ROW NUM
        self.y = y
        self.bfs_step_num = "x"

        # GAME FIELDS
        self.door = NO_DOOR
        self.door_key = False
        self.monsters = []
        self.treasure_chest = 0
        self.non_interactive = []
        self.interactive = []

    


# EoF
