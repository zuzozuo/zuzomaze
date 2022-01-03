import random
from consts import *
import pygame


class Cell():
    def __init__(self, width, height, id, x, y):
        self.width = width
        self.height = height
        self.id = id
        self.walls = WALL_TOP + WALL_RIGHT + WALL_BOTTOM + WALL_LEFT + CELL_NOT_VISITED
        self.x = x  #x = id - (id // width) * width  np y = 93 - (93 /10 ) * 10 = 3 X -> COL NUMBER
        self.y = y  #y = id // maze_width - np x = 9 / 10 = 0  Y-> ROW NUMBER


class Maze():
    def __init__(self, rows, cols, start):
        self.rows = rows
        self.cols = cols
        self.cells = [Cell (CELL_WIDTH, CELL_HEIGHT, i,  (i - (i // rows) * rows), (i // rows)) for i in range(0, (rows * cols))]
        self.stack = [self.cells[start]]
        self.finished_maze = []
        

    def display_cells(self):
        for cell in self.cells:
            print("id: " + str(cell.id) + " x: " + str(cell.x) + " y: " + str(cell.y) + " wall_value: " + str(bin(cell.walls)))
    
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


#--------------------
    def reset_visit_flag(self):
        for i in range(0, len(self.cells)):
            self.cells[i].walls &= ~CELL_VISITED; 

    def get_cells(self):
        return self.cells
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




#----------------------------------
def randomize_endpoints(self): #selects start and endpoint randomly
    #start cell index
        s_c = 0 
    #goal cell index
        g_c = random.randint(int((len(self.cells)/4) * 3), len(self.cells)-1)

        self.cells[s_c].walls |= CELL_IS_START
        self.cells[g_c].walls |= CELL_IS_GOAL

        return(s_c, g_c)



