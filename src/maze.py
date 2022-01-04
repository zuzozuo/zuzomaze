import random
from cell import Cell
from consts import (CELL_WIDTH, CELL_HEIGHT, W_TOP, W_RIGHT, W_BOTTOM, W_LEFT,
                    CELL_VISITED, CELL_START, CELL_GOAL, CELL_PATH)


class Maze():
    def __init__(self, rows, cols, start):
        self.rows = rows
        self.cols = cols
        self.cells = [Cell(CELL_WIDTH, CELL_HEIGHT, i,
                      (i - (i // rows) * rows), (i // rows)) for i in range(0, (rows * cols))]

        self.stack = [self.cells[start]]
        self.finished_maze = []
        self.start = start

# ------------- DISPLAY METHODS
    def display_cells(self):

        for cell in self.cells:
            walls = str(bin(cell.walls))
            print("id: {} x: {} y: {} wall: {}".format(cell.id, cell.x, cell.y, walls))

# --------------BINARY PREVIEW OF GENERATED MAZE - WITHOUT BFS!
    def display_maze(self):

        current = self.cells[0].id

        for y in range(self.cols):
            row = [''] * 2

            for x in range(self.rows):
                cell = self.cells[current + x]
                row[0] += '00' if (cell.walls & W_TOP) else '01'
                row[1] += '01' if (cell.walls & W_LEFT) else '11'

            current += self.rows
            [self.finished_maze.append((str + '0')) for str in row]

        self.finished_maze.append('0' * (self.rows * 2 + 1))

        for line in self.finished_maze:
            print(line)

# --------------- REVERSE BACKTRACKING MAZE GENERATION
    def check_neighbours(self, current):
        neighbours = []
        x = current.x
        y = current.y
        id = current.id
        # TOP
        if (y > 0) and not (self.cells[id - self.rows].walls & CELL_VISITED):
            neighbours.append(self.cells[id - self.rows])

        # RIGHT
        if (x < self.rows - 1) and not (self.cells[id + 1].walls & CELL_VISITED):
            neighbours.append(self.cells[id + 1])

        # BOTTOM
        if (y < (self.cols - 1)) and not (self.cells[id + self.rows].walls & CELL_VISITED):
            neighbours.append(self.cells[id + self.rows])

        # LEFT
        if (x > 0) and not (self.cells[id - 1].walls & CELL_VISITED):
            neighbours.append(self.cells[id - 1])

        return neighbours

    def generate(self):
        while(len(self.stack) > 0):
            current = self.stack.pop()

            # check for unvisited neighbours of the current cell
            neighbours = self.check_neighbours(current)

            if (len(neighbours) > 0):
                # push the current cell on to the stack
                self.stack.append(current)
                # chose one of the unvisited neighbours
                visit = random.choice(neighbours)

                # emove the wall between current and currently visited cell
                diff = visit.id - current.id

                # TOP
                if (diff == -self.rows):
                    self.cells[current.id].walls &= ~W_TOP
                    self.cells[visit.id].walls &= ~W_BOTTOM
                # RIGHT
                elif (diff == 1):
                    self.cells[current.id].walls &= ~W_RIGHT
                    self.cells[visit.id].walls &= ~W_LEFT
                # BOTTOM
                elif (diff == self.rows):
                    self.cells[current.id].walls &= ~W_BOTTOM
                    self.cells[visit.id].walls &= ~W_TOP
                # LEFT
                elif (diff == -1):
                    self.cells[current.id].walls &= ~W_LEFT
                    self.cells[visit.id].walls &= ~W_RIGHT
                else:
                    print("Something went wrong!!")
                    return

                # mark the chosen cell as visited and push the cell on to the stack
                self.cells[visit.id].walls |= CELL_VISITED
                self.stack.append(visit)

# -----------------------HELPERS
    def get_cells(self):
        return self.cells

# --------------------BFS SHORTEST PATH SEARCH
    def randomize_endpoints(self):   # selects start and endpoint id randomly
        # start cell index
        s_c = self.start

        # goal cell index
        g_c = random.randint(int((len(self.cells)/2)), len(self.cells)-1)

        self.cells[s_c].walls |= CELL_START
        self.cells[g_c].walls |= CELL_GOAL

        return(s_c, g_c)

    def find_bfs_neighbours(self, current):
        x = current.x
        y = current.y
        id = current.id
        neighbours = []

        # TOP
        if (y > 0) and not((self.cells[id - self.rows].walls & W_BOTTOM) or (current.walls & W_TOP)):
            neighbours.append(self.cells[id - self.rows])

        # RIGHT
        if (x < self.rows - 1) and not((self.cells[id + 1].walls & W_LEFT) or (current.walls & W_RIGHT)):
            neighbours.append(self.cells[id + 1])

        # BOTTOM
        if (y < (self.cols - 1)) and not((self.cells[current.id + self.rows].walls & W_TOP) or (current.walls & W_BOTTOM)):
            neighbours.append(self.cells[id + self.rows])

        # LEFT
        if (x > 0) and not((self.cells[id - 1].walls & W_RIGHT) or (current.walls & W_LEFT)):
            neighbours.append(self.cells[id - 1])

        return neighbours

    def find_path(self):
        start, goal = self.randomize_endpoints()
        queue = []
        searched = []
        backtrace = {}

        queue = [start]

        while(queue):
            current = queue.pop(0)   # FIFO

            if(current == goal):
                break

            neighbours = self.find_bfs_neighbours(self.cells[current])

            for i in range(0, len(neighbours)):
                check = neighbours[i].id

                if (check not in searched):
                    # remebering visited cells
                    searched.append(check)
                    # how did we get to the next cell?
                    backtrace[check] = current
                    queue.append(check)

            # print("Current: " + str(current))
            # print("Neighbours: " + str([neighbour.id for neighbour in neighbours]))

        if (current == goal):
            path = [goal]
            current = goal

            while(current != start):
                current = backtrace[current]
                path.insert(0, current)

            for i in range(0, len(path)):
                self.cells[path[i]].walls |= CELL_PATH
                self.cells[path[i]].bfs_step_num = str(i)

            self.cells[start].bfs_step_num = "S"
            self.cells[goal].bfs_step_num = "G"

            return True

        else:
            return False
# EoF
