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
        self.is_start = False
        self.is_goal = False
        self.bfs_visit = False #for colouring
        self.bfs_path = False #for colouring


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




# #----------------------------------
#  def randomize_endpoints(self): #selects start and endpoint randomly
#     #start cell index
#         s_c = 0 
#     #goal cell index
#         g_c = random.randint(int((len(self.cells)/4) * 3), len(self.cells)-1)

#         self.cells[s_c].is_start = True
#         self.cells[g_c].is_goal = True 

#         return(s_c, g_c)


#     def solve_maze(self): #bfs

#         queue = []
#         visited = []
#         neighbours= []
#         backtrace = {}
    
#     #initializing enpoints
#         s_c, g_c = self.randomize_endpoints() 
#         start = self.cells[s_c]
#         goal = self.cells[g_c]

#         print(start.id)
#         print(goal.id)
    
#     #reset visit flags for neighbour searching
#         self.reset_visit_flag()

#         queue.append(start)

#         while(len(queue) > 0):
#             current = queue.pop(0)
#             #print(len(queue))

#             if current.id == goal.id:
#                 print("Reached the Goal")
#                 break
            

#             #checking neighbours
#             x = current.x
#             y = current.y

#             #top
#             if(y > 0 and ~(current.walls & WALL_TOP) and ~(self.cells[current.id - self.width].walls & WALL_TOP)):
#                 neighbours.append(self.cells[current.id - self.width])

#             #right
#             if (( x < self.width -1 ) and ~(current.walls & WALL_RIGHT)  and ~(self.cells[current.id + 1].walls & WALL_RIGHT)):
#                 neighbours.append(self.cells[current.id + 1 ])

            
#             #bottom
#             if ( y < (self.height - 1) )  and ~(current.walls & WALL_BOTTOM) and ~(self.cells[current.id + self.width].walls & WALL_BOTTOM ):
#                 neighbours.append(self.cells[current.id + self.width])


#             #left
#             if( ( x > 0 )  and ~(current.walls & WALL_LEFT) and ~(self.cells[current.id - 1].walls & WALL_LEFT)):
#                 neighbours.append(self.cells[current.id - 1])

#             #------------------------
#             for i in range(0, len(neighbours)):
#                 check = neighbours[i]

#                 if(~(neighbours[i].walls & CELL_VISITED)):
#                     neighbours[i].walls |= CELL_VISITED
#                     backtrace[str(check.id)] = current.id
#                     queue.append(check)

#             neighbours_id = [cell.id for cell in neighbours]
#             print("Current id: " + str(current.id) + " x: " + str(x) + " y: " + str(y))
#             print("Neighbours: " + str(neighbours_id))
            
#             neighbours = []
        

#         # if(current.id == goal.id):
#         #     path = [goal]
#         #     current = goal
#         #     print(current.id)
#         #     print(start.id)
#         #     print("==")
#         #     print(backtrace)
#         #   #  while(current.id != start.id):
#         #   #      current = backtrace[str(current.id)]
#         #   #      path.insert(0, current)
#         #   #      print(path)

            
#         #     if(len(path) > 2):
#         #         for i in range(0, len(path)):
#         #             print(path)
#         #             self.cells[path[i].id].walls |=CELL_BFS_PATH
#         #     print("Supcio!")

#             #neighbours = self.check_neighbours(self.cells[current]) """

            

                


