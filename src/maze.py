import random
from consts import *


class Cell():
    def __init__(self, width, height, id, x, y):
        self.width = width
        self.height = height
        self.id = id
        self.walls = WALL_TOP + WALL_RIGHT + WALL_BOTTOM + WALL_LEFT + CELL_NOT_VISITED
        self.x = x  #x = id // maze_width - np x = 9 / 10 = 0
        self.y = y  #y = id - (id // width) * width  np y = 93 - (93 /10 ) * 10 = 3


class Maze():
    def __init__(self, width, height, start):
        self.width = width
        self.height = height 
        self.cells = [Cell (CELL_WIDTH, CELL_HEIGHT, i, (i - (i // width) * width), (i // width)) for i in range(0, (width * height))]
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
        if ( y > 0 ) and not (self.cells[current.id - self.width].walls & CELL_VISITED):
            neighbours.append(self.cells[current.id  - self.width ])
        
        #RIGHT
        if ( x < self.width -1 ) and not (self.cells[current.id + 1].walls & CELL_VISITED):
            neighbours.append(self.cells[current.id + 1 ])

        #BOTTOM
        if ( y < (self.height - 1) ) and not (self.cells[current.id + self.width].walls & CELL_VISITED):
            neighbours.append(self.cells[current.id  + self.width ])

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
                if (diff == -self.width):
                    self.cells[current.id].walls &= ~WALL_TOP
                    self.cells[visit.id].walls &= ~WALL_BOTTOM
                #RIGHT
                elif (diff == 1):
                    self.cells[current.id].walls &= ~WALL_RIGHT
                    self.cells[visit.id].walls &= ~WALL_LEFT
                #BOTTOM
                elif (diff == self.width):
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

#--------------TO_EDIT
    def display_maze(self):

        current = self.cells[0].id

        for y in range(self.height):
            row = [''] * 2

            for x in range(self.width):
                cell = self.cells[current + x]
                row[0] += '00' if (cell.walls & WALL_TOP) else '01'
                row[1] += '01' if (cell.walls & WALL_LEFT) else '11'

            current += self.width
            [self.finished_maze.append((str + '0')) for str in row]

        self.finished_maze.append('0' * (self.width * 2 + 1))

        for line in self.finished_maze:
            print(line)



