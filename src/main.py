from consts import *
from maze import Maze
import pygame
from pygame.locals import *
from PIL import Image, ImageDraw

#--------------------------------------------------


def pygame_draw(cells):

    pygame.init()  
    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    font1 = pygame.font.SysFont(FONT_NAME, 10)

    running = True

    while running: 
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        
        for i in range(0, len(cells)):
            img = font1.render(str(cells[i].id), True, C_BLACK)
            x = cells[i].x
            y = cells[i].y

            if (cells[i].walls & CELL_IS_START) | (cells[i].walls & CELL_IS_GOAL):
                pygame.draw.rect(surface, C_ENDPOINT , pygame.Rect(x *CELL_WIDTH, y *CELL_HEIGHT , CELL_WIDTH, CELL_HEIGHT)) 
            elif cells[i].walls & CELL_BFS_PATH:
                pygame.draw.rect(surface, C_VISITED_2 , pygame.Rect(x *CELL_WIDTH, y *CELL_HEIGHT , CELL_WIDTH, CELL_HEIGHT)) 
            elif cells[i].walls & CELL_VISITED:
                pygame.draw.rect(surface, C_VISITED , pygame.Rect(x *CELL_WIDTH, y *CELL_HEIGHT , CELL_WIDTH, CELL_HEIGHT)) 
            else:
                pygame.draw.rect(surface, C_NORMAL , pygame.Rect(x *CELL_WIDTH, y *CELL_HEIGHT , CELL_WIDTH, CELL_HEIGHT))


        #top line
            if(cells[i].walls & WALL_TOP):
                pygame.draw.line(surface, C_WHITE, (x * CELL_WIDTH, y * CELL_WIDTH),                     ((x * CELL_WIDTH) + CELL_WIDTH, y * CELL_HEIGHT), BORDER_THICKNESS)

        #right line
            if(cells[i].walls & WALL_RIGHT):
                pygame.draw.line(surface, C_WHITE, ((x * CELL_WIDTH) + CELL_WIDTH  , y * CELL_HEIGHT),   ((x * CELL_WIDTH) + CELL_WIDTH , (y * CELL_HEIGHT) + CELL_HEIGHT), BORDER_THICKNESS)

        #bottom line
            if(cells[i].walls & WALL_BOTTOM):
                pygame.draw.line(surface, C_WHITE, (x * CELL_WIDTH , (y * CELL_HEIGHT) + CELL_HEIGHT),                   ((x * CELL_WIDTH) + CELL_WIDTH,  (y * CELL_HEIGHT) + CELL_HEIGHT),  BORDER_THICKNESS)

        #left line
            if(cells[i].walls & WALL_LEFT):
                pygame.draw.line(surface, C_WHITE, (x * CELL_WIDTH , y * CELL_HEIGHT),                   (x * CELL_WIDTH , (y  * CELL_HEIGHT) + CELL_HEIGHT) , BORDER_THICKNESS)
            
            surface.blit(img, (x * CELL_WIDTH + 5 , y * CELL_WIDTH + 5))

        pygame.display.flip()

#-------------------------------------------------------
#----TO EDIT
def draw_image(cells , cols, rows):
    size_x = cols * CELL_BOX_SIZE + IMG_MARGIN * 2
    size_y = rows * CELL_BOX_SIZE + IMG_MARGIN * 2
    img = Image.new('RGB', (size_x, size_y))
    draw = ImageDraw.Draw(img)


    draw.rectangle([
        (IMG_MARGIN, IMG_MARGIN), 
        (IMG_MARGIN + cols * CELL_BOX_SIZE, IMG_MARGIN + rows * CELL_BOX_SIZE)],
        fill=C_NORMAL, outline=C_WHITE)

    curr_pos = 0
    x = IMG_MARGIN  #startposition
    y = IMG_MARGIN  #startposition


    for posy in range(0, rows):
        for posx in range(0, cols):
            cell = cells[curr_pos + posx]
            break
        break
    pass


#-------------------------------------------------------
test = Maze(MAZE_COLS, MAZE_ROWS, 0)
test.generate()
test.find_path()
print("---------------------------------------------")
cells = test.get_cells()
#pygame_draw(cells)
#test.display_cells()
#test.display_maze()