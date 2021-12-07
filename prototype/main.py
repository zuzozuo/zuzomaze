import pygame
from pygame.locals import *
from cell import Cell
from map import Map

#-------------------------------------
CELL_WIDTH = 100
CELL_HEIGHT = 100
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
BORDER_THICKNESS = 2
ROWS = (int)(WINDOW_HEIGHT // CELL_HEIGHT)
COLS = (int)(WINDOW_WIDTH // CELL_WIDTH)

#-------------------------------------
map = Map(ROWS, COLS, CELL_WIDTH, CELL_HEIGHT)
cells = map.init_cells()

    


#-----------------------------------------------
pygame.init()  
surface = pygame.display.set_mode((WINDOW_WIDTH + 3, WINDOW_HEIGHT + 10))
color = (255,0,0)
blue = (0,0,255)
running = True

#-----------------------------------------------
while running: 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    
    for i in range(0, len(cells)):
        x = cells[i].x
        y = cells[i].y

    #top line
        if(cells[i].walls[0]):
            pygame.draw.line(surface, color, (x * CELL_WIDTH, y * CELL_WIDTH),                     ((x * CELL_WIDTH) + CELL_WIDTH, y * CELL_HEIGHT), BORDER_THICKNESS)

    #right line
        if(cells[i].walls[1]):
            pygame.draw.line(surface, color, ((x * CELL_WIDTH) + CELL_WIDTH  , y * CELL_HEIGHT),   ((x * CELL_WIDTH) + CELL_WIDTH , (y * CELL_HEIGHT) + CELL_HEIGHT), BORDER_THICKNESS)

    #bottom line
        if(cells[i].walls[2]):
            pygame.draw.line(surface, color, (x * CELL_WIDTH , (y * CELL_HEIGHT) + CELL_HEIGHT),                   ((x * CELL_WIDTH) + CELL_WIDTH,  (y * CELL_HEIGHT) + CELL_HEIGHT),  BORDER_THICKNESS)

    #left line
        if(cells[i].walls[3]):
            pygame.draw.line(surface, color, (x * CELL_WIDTH , y * CELL_HEIGHT),                   (x * CELL_WIDTH , (y  * CELL_HEIGHT) + CELL_HEIGHT) , BORDER_THICKNESS)

       


    pygame.display.flip()

#----------------------------------------------------