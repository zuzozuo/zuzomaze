import random
from consts import *
from collections import deque

class Cell():
    def __init__(self, width, height, id, x, y):
        self.width = width
        self.height = height
        self.id = id
        self.walls = WALL_TOP + WALL_RIGHT + WALL_BOTTOM + WALL_LEFT + CELL_NOT_VISITED
        self.x = x  #x = id - (id // width) * width  np y = 93 - (93 /10 ) * 10 = 3 X -> COL NUMBER
        self.y = y  #y = id // maze_width - np x = 9 / 10 = 0  Y-> ROW NUMBER
        self.bfs_visited = False


class Maze():
    def __init__(self, rows, cols, start):
        self.rows = rows
        self.cols = cols
        self.cells = [Cell (CELL_WIDTH, CELL_HEIGHT, i,  (i - (i // rows) * rows), (i // rows)) for i in range(0, (rows * cols))]
        self.stack = [self.cells[start]]
        self.finished_maze = []
        
        
#------------- DISPLAY METHODS
    def display_cells(self):
        for cell in self.cells:
            print("id: " + str(cell.id) + " x: " + str(cell.x) + " y: " + str(cell.y) + " wall_value: " + str(bin(cell.walls)))

#--------------TO_EDIT
    def display_maze(self):

        current = self.cells[0].id

        for y in range(self.cols):
            row = [''] * 2

            for x in range(self.rows):
                cell = self.cells[current + x]
                row[0] += '00' if (cell.walls & WALL_TOP) else '01'
                row[1] += '01' if (cell.walls & WALL_LEFT) else '11'

            current += self.rows
            [self.finished_maze.append((str + '0')) for str in row]

        self.finished_maze.append('0' * (self.rows * 2 + 1))

        for line in self.finished_maze:
            print(line)

#--------------- REVERSE BACKTRACKING MAZE GENERATION
    
    def check_neighbours(self, current):
        neighbours = []
        x = current.x
        y = current.y
        #TOP
        if ( y > 0 ) and not (self.cells[current.id - self.rows].walls & CELL_VISITED):
            neighbours.append(self.cells[current.id  - self.rows ])
        
        #RIGHT
        if ( x < self.rows -1 ) and not (self.cells[current.id + 1].walls & CELL_VISITED):
            neighbours.append(self.cells[current.id + 1 ])

        #BOTTOM
        if ( y < (self.cols - 1) ) and not (self.cells[current.id + self.rows].walls & CELL_VISITED):
            neighbours.append(self.cells[current.id  + self.rows ])

        #LEFT
        if ( x > 0 ) and not (self.cells[current.id - 1].walls & CELL_VISITED):
            neighbours.append(self.cells[current.id - 1 ])
        
        return neighbours
        

    def generate(self):
        while(len(self.stack) > 0):
            current = self.stack.pop()
            
            #check for unvisited neighbours of the current cell
            neighbours = self.check_neighbours(current)


            if(len(neighbours) > 0):
                #push the current cell on to the stack
                self.stack.append(current)
                #chose one of the unvisited neighbours
                visit = random.choice(neighbours)

                #remove the wall between current and currently visited cell
                diff = visit.id - current.id

                #TOP
                if (diff == -self.rows):
                    self.cells[current.id].walls &= ~WALL_TOP
                    self.cells[visit.id].walls &= ~WALL_BOTTOM
                #RIGHT
                elif (diff == 1):
                    self.cells[current.id].walls &= ~WALL_RIGHT
                    self.cells[visit.id].walls &= ~WALL_LEFT
                #BOTTOM
                elif (diff == self.rows):
                    self.cells[current.id].walls &= ~WALL_BOTTOM
                    self.cells[visit.id].walls &= ~WALL_TOP
                #LEFT
                elif (diff == -1):
                    self.cells[current.id].walls &= ~WALL_LEFT
                    self.cells[visit.id].walls &= ~WALL_RIGHT
                else:
                    print("OOPSIE!!")
                    return

                #mark the chosen cell as visited and push the cell on to the stack
                self.cells[visit.id].walls |=CELL_VISITED
                self.stack.append(visit)    


#-----------------------HELPERS
    def reset_visit_flag(self):
        for i in range(0, len(self.cells)):
            self.cells[i].walls &= ~CELL_VISITED; 

    def get_cells(self):
        return self.cells


#--------------------BFS SHORTEST PATH SEARCH 
    def randomize_endpoints(self): #selects start and endpoint randomly
        #start cell index
            s_c = 0 
        #goal cell index
            g_c = random.randint(int((len(self.cells)/4) * 3), len(self.cells)-1)

            self.cells[s_c].walls |= CELL_IS_START
            self.cells[g_c].walls |= CELL_IS_GOAL

            return(s_c, g_c)


    def find_bfs_neighbours(self, current):
        x = current.x
        y = current.y
        neighbours = []

        # has_t_w = current.walls & WALL_TOP
        # has_b_w = self.cells[current.id - self.rows].walls & WALL_BOTTOM
        # print(str(bin(current.walls)))
        # print(str(bin(self.cells[current.id - self.rows].walls)))
        # print(str(bin(has_t_w)))
        # print(str(bin(has_b_w)))
        # print(str(bin(has_t_w & has_b_w)))
        # print(str(bin(~(has_t_w & has_b_w))))
        #TOP
        if ( y > 0 ) and not((self.cells[current.id - self.rows].walls & WALL_BOTTOM) or (current.walls & WALL_TOP)):
            neighbours.append(self.cells[current.id  - self.rows ])
            
        #RIGHT
        if ( x < self.rows -1 ) and not((self.cells[current.id + 1].walls & WALL_LEFT) or (current.walls & WALL_RIGHT)):
            neighbours.append(self.cells[current.id + 1 ])

        #BOTTOM
        if ( y < (self.cols - 1) ) and not((self.cells[current.id + self.rows].walls & WALL_TOP) or (current.walls & WALL_BOTTOM)):
            neighbours.append(self.cells[current.id  + self.rows ])

        #LEFT
        if ( x > 0 ) and not((self.cells[current.id - 1].walls & WALL_RIGHT) or (current.walls & WALL_LEFT)):
            neighbours.append(self.cells[current.id - 1 ])

        return neighbours

    def find_path(self):
        s_c, g_c = self.randomize_endpoints()
        start = self.cells[s_c]
        goal = self.cells[g_c]
        queue = deque()
        searched = []
        backtrace = {}
#try to do it on ids and then generate proper flags maybe?

        queue.append(start.id)

        while(queue):
            current = queue.popleft() #FIFO

            if(current== goal.id):
                break

            neighbours = self.find_bfs_neighbours(self.cells[current])

            for i in range(0, len(neighbours)):
                check = neighbours[i].id
                
                if(not check in searched):
                    searched.append(check)
                    backtrace[check] = current
                    queue.append(check)

        

        
            print("Current: " + str(current))
            print("Neighbours: " + str([neighbour.id for neighbour in neighbours]))
        
        
        if(current == goal.id):
            print(backtrace)
            path = [goal.id]
            current = goal.id

            while(current != start.id):
                current = backtrace[current]
                path.insert(0, current)

            for i in path:
                self.cells[i].walls |= CELL_BFS_PATH
                print(str(bin(self.cells[i].walls & CELL_BFS_PATH)))
            
            print(path)
            

            print("Woohoe!")
            
        else:
            print("Brak trasy")
        







