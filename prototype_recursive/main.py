import pygame
from pygame.locals import *
from cell import Cell
from map import Map
import  sys

sys.setrecursionlimit(10000)

#-------------------------------------
CELL_WIDTH = 25
CELL_HEIGHT = 25
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
BORDER_THICKNESS = 2
ROWS = (int)(WINDOW_HEIGHT // CELL_HEIGHT)
COLS = (int)(WINDOW_WIDTH // CELL_WIDTH)
C_VISITED = (102, 170, 255)
C_BLUE  = (0, 0, 255)
C_WHITE = (255, 255, 255)

#--------------------------------------- FUNCTION TO DELETE LATER

def generate_maze(cells, current, map):

    current.visited = True 
    x = current.x
    y = current.y

    top = None
    right = None
    bottom = None
    left = None

    top_index = map.index(x, y -1)
    right_index = map.index(x + 1, y)
    bottom_index = map.index(x, y + 1)
    left_index = map.index(x-1, y)

    print("top_index: " + str(top_index))
    print("right_index: " + str(right_index))
    print("bottom_index: " + str(bottom_index))
    print("left_index: " + str(left_index))
    print("-------------------------------")

    if (top_index is not None):
        top = cells[top_index]
    if (right_index is not None):
        right = cells[right_index]
    if (bottom_index is not None):
        bottom = cells[bottom_index]
    if (left_index is not None):
        left = cells[left_index]

    next = current.checkNeighbors(top, right, bottom, left)
    if (next is not None):
        next.visited = True
        map.stack.append(current)
#-------------------
        current.isCurrent = False #ILLEGAL!!
        next.isCurrent = True #ILLEGAL
#----------------------------
        map.removeWalls(current, next)

        return generate_maze(cells, next, map)

    elif (len(map.stack) > 0): 
        current.isCurrent = False #ILLEGAL
        current = map.stack.pop()
        current.isCurrent = True #ILLEGAL
        return generate_maze(cells, current, map)

    return None

   # if (next):
   #     next.visited = True
   #     current = next
   #     generate_maze(cells, current)
#-------------------------------------
map = Map(ROWS, COLS, CELL_WIDTH, CELL_HEIGHT)

cells = map.init_cells()
current = cells[0]
current.isCurrent = True #illegal!!!!! TO DELETE LATER
next = cells[0]

#-----------------------------------------------
pygame.init()  
surface = pygame.display.set_mode((WINDOW_WIDTH + 3, WINDOW_HEIGHT + 10))
running = True

generate_maze(cells, current, map)

#-----------------------------------------------
while running: 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    
    for i in range(0, len(cells)):
        x = cells[i].x
        y = cells[i].y

        if cells[i].visited:  #change color
            pygame.draw.rect(surface, C_VISITED , pygame.Rect(x *CELL_WIDTH, y *CELL_HEIGHT , CELL_WIDTH, CELL_HEIGHT)) 
        else:
             pygame.draw.rect(surface, (0,102,255) , pygame.Rect(x *CELL_WIDTH, y *CELL_HEIGHT , CELL_WIDTH, CELL_HEIGHT)) 
        
        if cells[i].isCurrent:
            pygame.draw.rect(surface, (50,230,255) , pygame.Rect(x *CELL_WIDTH, y *CELL_HEIGHT , CELL_WIDTH, CELL_HEIGHT)) 


    #top line
        if(cells[i].walls[0]):
            pygame.draw.line(surface, C_WHITE, (x * CELL_WIDTH, y * CELL_WIDTH),                     ((x * CELL_WIDTH) + CELL_WIDTH, y * CELL_HEIGHT), BORDER_THICKNESS)

    #right line
        if(cells[i].walls[1]):
            pygame.draw.line(surface, C_WHITE, ((x * CELL_WIDTH) + CELL_WIDTH  , y * CELL_HEIGHT),   ((x * CELL_WIDTH) + CELL_WIDTH , (y * CELL_HEIGHT) + CELL_HEIGHT), BORDER_THICKNESS)

    #bottom line
        if(cells[i].walls[2]):
            pygame.draw.line(surface, C_WHITE, (x * CELL_WIDTH , (y * CELL_HEIGHT) + CELL_HEIGHT),                   ((x * CELL_WIDTH) + CELL_WIDTH,  (y * CELL_HEIGHT) + CELL_HEIGHT),  BORDER_THICKNESS)

    #left line
        if(cells[i].walls[3]):
            pygame.draw.line(surface, C_WHITE, (x * CELL_WIDTH , y * CELL_HEIGHT),                   (x * CELL_WIDTH , (y  * CELL_HEIGHT) + CELL_HEIGHT) , BORDER_THICKNESS)
        
        


    pygame.display.flip()

#----------------------------------------------------