from consts import *
from maze import Maze
import pygame
from pygame.locals import *
from PIL import Image, ImageDraw, ImageFont
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
def draw_image(cells , rows, cols):
    size_x = rows * CELL_BOX_SIZE + IMG_MARGIN * 2  #ROWS  - DRAWING FROM LEFT TO RIGHT 
    size_y = cols * CELL_BOX_SIZE + IMG_MARGIN * 2  #COLS - DRAWING FROM UP TO DOWN
    img = Image.new('RGB', (size_x, size_y))
    draw = ImageDraw.Draw(img)
    txt_font = ImageFont.truetype("arial.ttf", FONT_SIZE)

    curr_pos = 0
    x = IMG_MARGIN  #startposition
    y = IMG_MARGIN  #startposition


    for posy in range(0, cols):
        for posx in range(0, rows):
            cell = cells[curr_pos + posx]
            x_txt = x + int(CELL_BOX_SIZE/3)
            y_txt =  y + int(CELL_BOX_SIZE/3)

            if(cell.walls & CELL_IS_START) | (cell.walls & CELL_IS_GOAL):
                draw.rectangle([(x,y), (x + CELL_BOX_SIZE, y + CELL_BOX_SIZE)], fill=C_ENDPOINT)
            elif (cell.walls & CELL_BFS_PATH):
                draw.rectangle([(x,y), (x + CELL_BOX_SIZE, y + CELL_BOX_SIZE)], fill=C_VISITED_2)
                draw.text((x_txt,y_txt), str(cell.bfs_step_num), fill=C_BLACK, font= txt_font)
            else:
                draw.rectangle([(x,y), (x + CELL_BOX_SIZE, y + CELL_BOX_SIZE)], fill=C_NORMAL)

            #draw.text((x_txt,y_txt), str(cell.id), fill=C_BLACK, font= txt_font)

            if (cell.walls & WALL_TOP):
                draw.line([(x,y), (x + CELL_BOX_SIZE, y)])

            if (cell.walls & WALL_RIGHT):
                draw.line([(x + CELL_BOX_SIZE , y), (x + CELL_BOX_SIZE, y + CELL_BOX_SIZE)])
            
            if (cell.walls & WALL_BOTTOM):
                draw.line([(x,y + CELL_BOX_SIZE), (x + CELL_BOX_SIZE, y + CELL_BOX_SIZE)])

            if (cell.walls & WALL_LEFT):
                draw.line([(x,y), (x , y + CELL_BOX_SIZE)])

            
            x += CELL_BOX_SIZE
        curr_pos += rows
        x = IMG_MARGIN
        y += CELL_BOX_SIZE
    img.show()
    img.save("test.png")



#-------------------------------------------------------
test = Maze(MAZE_WIDTH_2, MAZE_HEIGHT_2, 0)
test.generate()
test.find_path()
print("---------------------------------------------")
cells = test.get_cells()
#test.display_cells()
#test.display_maze()

draw_image(cells, MAZE_WIDTH_2, MAZE_HEIGHT_2)
#pygame_draw(cells)
#test.display_cells()
#test.display_maze()