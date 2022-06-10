import random
import json
from random import random as rnd
from cell import Cell
from consts import (CELL_SIZE, D_TOP, D_RIGHT, D_BOTTOM, D_LEFT,  W_TOP, W_RIGHT, W_BOTTOM, W_LEFT,
                    CELL_VISITED, CELL_START, CELL_GOAL, CELL_PATH)


class Maze():
    def __init__(self, rows, cols, start):
        self.rows = rows # x 
        self.cols = cols # y
        self.cells = [Cell(CELL_SIZE, i,
                      (i - (i // rows) * rows), (i // rows)) for i in range(0, (rows * cols))]

        self.stack = [self.cells[start]]
        self.finished_maze = []
        self.start = start
        self.path =[] # contains id of cells that are leading to the goal

# ------------- DISPLAY METHODS
    def display_cells(self):

        for cell in self.cells:
            walls = str(bin(cell.walls))
            print("id: {} x: {} y: {} wall: {}".format(cell.id, cell.x, cell.y, walls))

# ------------- REVERSE BACKTRACKING MAZE GENERATION
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

                # remove the wall between current and currently visited cell
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

# ------------- HELPERS
    def get_cells(self):
        return self.cells

# ------------- BFS SHORTEST PATH SEARCH
    def randomize_endpoints(self):   # selects start and endpoint id randomly
        # start cell index
        s_c = self.start

        # goal cell index
        # g_c = random.randint(int((len(self.cells)/2)), len(self.cells)-1)
        g_c = len(self.cells)-1 # assigning goal as last cell in the maze 

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
        if (y < (self.cols - 1)) and not((self.cells[id + self.rows].walls & W_TOP) or (current.walls & W_BOTTOM)):
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

            # self.path  = [self.cells[id] for id in path]
            self.path = path
            return True

        else:
            return False

#  ------- ZUZOGEON HELPERS

    def add_door_randomly(self):
        door_q = random.randint(int(len(self.cells)/5)+1, int(len(self.cells)/2)-1) # door quantity - how many doors we want in our map?
        rand_cell_id = [random.randint(1, len(self.cells)-1) for x in range (0,door_q) ] # indexes  of random  cells that we want to edit

        while len(set(rand_cell_id)) != door_q:
            rand_cell_id.append(random.randint(1, len(self.cells)-1))

        rand_cell_id = set(rand_cell_id)


        for x in rand_cell_id:
            c = self.cells[x] 
            if (c.y > 0) and not (c.walls & W_TOP) and (rnd() < 0.5) and not (self.cells[x-self.rows].door & D_BOTTOM):
                c.door |= D_TOP

            if (c.x < self.rows - 1) and not (c.walls & W_RIGHT) and (rnd() < 0.5) and not (self.cells[x+1].door & D_LEFT):
                c.door |= D_RIGHT

            if (c.y < (self.cols - 1)) and not (c.walls & W_BOTTOM) and (rnd() < 0.5) and not (self.cells[x+self.rows].door & D_TOP):
                c.door |= D_BOTTOM

            if (c.x > 0) and not (c.walls & W_LEFT) and (rnd() < 0.5) and not (self.cells[x-1].door & D_RIGHT):
                c.door |= D_LEFT

            c.door_key = 1
    
    def add_entities_randomly(self):  # temporary function
        monsters_q = random.randint(int(len(self.cells)/5)+1, int(len(self.cells)/2)-1)
        treasure_chest_q = random.randint(int(len(self.cells)/5)+1, int(len(self.cells)/2)-1)
        rand_m_c_id = [random.randint(1, len(self.cells)-1) for x in range (0,monsters_q) ]
        rand_tc_c_id = [random.randint(1, len(self.cells)-1) for x in range (0,treasure_chest_q) ]

        while len(set(rand_m_c_id)) != monsters_q :
            rand_m_c_id.append(random.randint(1, len(self.cells)-1))

        while len(set(rand_tc_c_id)) != treasure_chest_q:
            rand_tc_c_id.append(random.randint(1, len(self.cells)-1))
        
        rand_m_c_id  = set(rand_m_c_id)
        rand_tc_c_id = set(rand_tc_c_id)
        
        for id in rand_m_c_id:
            self.cells[id].monsters = 1
        
        for id in rand_tc_c_id:
            self.cells[id].treasure_chest = 1

    
    def add_non_interactive_objects(self):
        non_int_obj = ["fairy", "stone", "table", "vase", "chair", "painting", "flower"]

        for x in range(0, len(self.cells)):
            q = random.randint(1, len(non_int_obj)-1)
            self.cells[x].non_interactive = [non_int_obj[random.randint(0, len(non_int_obj)-1)] for _ in range(0, q)]
        
    
    def add_door_key(self):
        door_cells = [c for c in self.cells if c.door]

        for d in door_cells:
            print("cell:  " + str(d.id)) 
            print("door:  " + str(format(d.door,'08b')))
            print("walls: " + str(format(d.walls,'08b')) + "\n")
            id = d.id
            x = d.x
            y = d.y
            # TODO zrob to kurwa w koncu debilu
            # # CHECK TOP
            # if (d.door & D_TOP) and (y > 0):
            #     self.cells[id-self.rows].door_key = 1
        
            # CHECK RIGHT
            if (d.door & D_RIGHT) and (d.x < self.rows - 1) and (d.walls & W_LEFT):
                self.cells[id-1].door_key = 1
            elif (d.door & D_RIGHT) and (d.x < self.rows - 1):
                pass
            # # CHECK BOTTOM
            # if (d.door & D_BOTTOM) and (d.y < (self.cols - 1)):
            #     self.cells[id+ self.rows].door_key = 1
            # # CHECK LEFT
            # if (d.door & D_LEFT) and (d.x > 0):
            #     self.cells[id-1].door_key = 1

        # neighbours = self.find_door_neighbours()

        # # for x in self.path:
        # #     if x in neighbours:
        # #         neighbours.remove(x)

        # # FOR CELLS IN PATH 
        # if [0, 1, 10] in self.path:
        #     self.cells[0].door_key = 1

        # for x in range(1, len(self.path)):
        #     if self.cells[self.path[x]].door:
        #         self.cells[self.path[x - 1]].door_key = 1
        
        # FOR CELLS NOT IN PATH - looking for neighbours 
        # for x in temp:
        #     self.cells[x].door_key = 1
        

    def find_door_neighbours(self):
        door_cells = [c for c in self.cells if c.door]
        neighbours = []

        for c in door_cells:
            x = c.x
            y = c.y
            id = c.id

            # TOP 
            if (y > 0) and (c.door & D_TOP) :
                neighbours.append(self.cells[id - self.rows].id)
            # RIGHT
            if (x < self.rows - 1) and (c.door & D_RIGHT):
                neighbours.append(self.cells[id + 1].id)

            # BOTTOM
            if (y < (self.cols - 1)) and (c.door & D_BOTTOM):
                neighbours.append(self.cells[id + self.rows].id)

            # LEFT
            if (x > 0) and (c.door & D_LEFT):
                neighbours.append(self.cells[id - 1].id)
        
        print(door_cells)
        print(neighbours)
            
        return neighbours
    
    def generate_json(self):
        map =[]

        for c in self.cells:
            door = [False, False, False, False]
            walls = [False, False, False, False]

            #  WALLS
            # TOP
            if (c.walls & W_TOP):
                walls[0] = True        

            # RIGHT
            if (c.walls & W_RIGHT):
                walls[1] = True

            # BOTTOM
            if (c.walls & W_BOTTOM):
                walls[2] = True

            # LEFT
            if (c.walls & W_LEFT):
                walls[3] = True
            
            # DOOR
            # TOP
            if (c.door & D_TOP):
                door[0] = True   

            # RIGHT
            if (c.door & D_RIGHT):
                door[1] = True   

            # BOTTOM
            if (c.door & D_BOTTOM):
                door[2] = True   

            # LEFT
            if (c.door & D_LEFT):
                door[3] = True   


            cell_dict = {
                "id": c.id,
                "x": c.x,
                "y": c.y,
                "key": c.door_key,
                "monsters": c.monsters,
                "non_inter": c.non_interactive,
                "door" : door,
                "walls": walls
            }

            map.append(cell_dict)

        map_dict = {"map": map }

        return json.dumps(map_dict)
    

            
# EoF
