from consts import (MAZE_WIDTH, MAZE_HEIGHT, CELL_SIZE, IMG_MARGIN, FONT_SIZE,
                    CELL_GOAL, CELL_START, CELL_PATH, C_NORMAL, C_ENDPOINT,
                    C_BLACK, C_VISITED_2, W_TOP, W_RIGHT, W_BOTTOM, W_LEFT)
from maze import Maze
from PIL import Image, ImageDraw, ImageFont
import random, string


def draw_image(cells, rows, cols, name):
    size_x = rows * CELL_SIZE + IMG_MARGIN * 2  # ROWS - DRAWING FROM L TO R
    size_y = cols * CELL_SIZE + IMG_MARGIN * 2  # COLS - DRAWING FROM U TO D
    img = Image.new('RGB', (size_x, size_y))
    draw = ImageDraw.Draw(img)
    txt_font = ImageFont.truetype("arial.ttf", FONT_SIZE)

    curr_pos = 0
    x = IMG_MARGIN  # start
    y = IMG_MARGIN  # start

    for posy in range(0, cols):
        for posx in range(0, rows):
            cell = cells[curr_pos + posx]
            x_txt = x + int(CELL_SIZE/3)
            y_txt = y + int(CELL_SIZE/3)

            if(cell.walls & CELL_START) | (cell.walls & CELL_GOAL):
                draw.rectangle([(x, y), (x + CELL_SIZE, y + CELL_SIZE)], fill=C_ENDPOINT)
                draw.text((x_txt, y_txt), str(cell.bfs_step_num), fill=C_BLACK, font=txt_font)

            elif (cell.walls & CELL_PATH):
                draw.rectangle([(x, y), (x + CELL_SIZE, y + CELL_SIZE)], fill=C_VISITED_2)

                draw.text((x_txt, y_txt), str(cell.bfs_step_num), fill=C_BLACK, font=txt_font)
            else:
                draw.rectangle([(x, y), (x + CELL_SIZE, y + CELL_SIZE)], fill=C_NORMAL)

            if (cell.walls & W_TOP):
                draw.line([(x, y), (x + CELL_SIZE, y)])

            if (cell.walls & W_RIGHT):
                draw.line([(x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE)])

            if (cell.walls & W_BOTTOM):
                draw.line([(x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE)])

            if (cell.walls & W_LEFT):
                draw.line([(x, y), (x, y + CELL_SIZE)])

            x += CELL_SIZE
        curr_pos += rows
        x = IMG_MARGIN
        y += CELL_SIZE

    img.show()
    img.save(name + "_maze.png")

# -------------------------------------------------------
# ----------------- MAIN

print("################################################")
print("#                 W E L C O M E                #")
print("#            I AM IMAGE MAZE GENERATOR         #")
print("# I can generate, solve and draw maze for you! #")
print("#            Project name: zuzomaze            #")
print("#           Author (github): zuzozuo           #")
print("#            It's aMAZEing  adventure!         #")
print("################################################")


aMAZEing = Maze(MAZE_WIDTH, MAZE_HEIGHT, 0)
aMAZEing.generate()
aMAZEing.find_path()
cells = aMAZEing.get_cells()

random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 7))  
draw_image(cells, MAZE_WIDTH, MAZE_HEIGHT, random_name)

# EoF
