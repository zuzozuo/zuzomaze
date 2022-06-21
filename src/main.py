from consts import (C_DOOR, C_RED, MAZE_WIDTH, MAZE_HEIGHT, CELL_SIZE, IMG_MARGIN, FONT_SIZE,
                    CELL_GOAL, CELL_START, CELL_PATH, C_NORMAL, C_ENDPOINT, C_WHITE, C_YELLOW, C_GRAY, C_BURGUNDY,
                    C_BLACK, C_VISITED_2, W_TOP, W_RIGHT, W_BOTTOM, W_LEFT, D_TOP,
                    D_BOTTOM, D_RIGHT, D_LEFT)
from maze import Maze
from PIL import Image, ImageDraw, ImageFont
import random, string

def draw_background(cells, rows, cols, name):
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
                draw.text((x_txt, y_txt), str(cell.id), fill=C_BLACK, font=txt_font)

            elif (cell.walls & CELL_PATH):
                draw.rectangle([(x, y), (x + CELL_SIZE, y + CELL_SIZE)], fill=C_VISITED_2)
                draw.text((x_txt, y_txt), str(cell.id), fill=C_BLACK, font=txt_font)
            

            else:
                draw.rectangle([(x, y), (x + CELL_SIZE, y + CELL_SIZE)], fill=C_NORMAL)
                draw.text((x_txt, y_txt), str(cell.id), fill=C_BLACK, font=txt_font)
            
            x += CELL_SIZE

        curr_pos += rows
        x = IMG_MARGIN
        y += CELL_SIZE

    return img

def draw_doors_and_walls(cells, rows, cols, name, img):
    draw = ImageDraw.Draw(img)

    curr_pos = 0
    x = IMG_MARGIN  # start
    y = IMG_MARGIN  # start

    for posy in range(0, cols):
        for posx in range(0, rows):
            cell = cells[curr_pos + posx]

            # DRAWING WALL LINES
            if (cell.walls & W_TOP):
                draw.line([(x, y), (x + CELL_SIZE, y)])

            if (cell.walls & W_RIGHT):
                draw.line([(x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE)])

            if (cell.walls & W_BOTTOM):
                draw.line([(x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE)])

            if (cell.walls & W_LEFT):
                draw.line([(x, y), (x, y + CELL_SIZE)])

            #DRAWING DOOR LINES
            if (cell.door & D_TOP):
                draw.line([(x, y), (x + CELL_SIZE, y)], fill=C_RED)

            if (cell.door & D_RIGHT):
                draw.line([(x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE)], fill=C_RED)

            if (cell.door & D_BOTTOM):
                draw.line([(x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE)], fill=C_RED)

            if (cell.door & D_LEFT):
                draw.line([(x, y), (x, y + CELL_SIZE)],fill=C_RED)
            
            x += CELL_SIZE

        curr_pos += rows
        x = IMG_MARGIN
        y += CELL_SIZE

    img.show()
    img.save(name + "_maze.png")


def draw_image(cells, rows, cols, name):
    img = draw_background(cells, rows, cols, name)
    draw_doors_and_walls(cells, rows, cols, name, img)

# ======
def draw_image_without_fill(cells, rows, cols, name):
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
                draw.rectangle([(x, y), (x + CELL_SIZE, y + CELL_SIZE)], fill=C_GRAY)
                draw.text((x_txt, y_txt), str(cell.id), fill=C_YELLOW, font=txt_font, stroke=5)

            elif (cell.walls & CELL_PATH):
                draw.text((x_txt, y_txt), str(cell.id), fill=C_YELLOW, font=txt_font, stroke=5)
            
            else:
                draw.text((x_txt, y_txt), str(cell.id), fill=C_GRAY, font=txt_font)

            # DRAWING WALL LINES
            if (cell.walls & W_TOP):
                draw.line([(x, y), (x + CELL_SIZE, y)])

            if (cell.walls & W_RIGHT):
                draw.line([(x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE)])

            if (cell.walls & W_BOTTOM):
                draw.line([(x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE)])

            if (cell.walls & W_LEFT):
                draw.line([(x, y), (x, y + CELL_SIZE)])

            #DRAWING DOOR LINES
            if (cell.door & D_TOP):
                draw.line([(x, y), (x + CELL_SIZE, y)], fill=C_BURGUNDY)

            if (cell.door & D_RIGHT):
                draw.line([(x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE)], fill=C_BURGUNDY)

            if (cell.door & D_BOTTOM):
                draw.line([(x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE)], fill=C_BURGUNDY)

            if (cell.door & D_LEFT):
                draw.line([(x, y), (x, y + CELL_SIZE)],fill=C_BURGUNDY)
            
            x += CELL_SIZE

        curr_pos += rows
        x = IMG_MARGIN
        y += CELL_SIZE

    img.show()
    img.save(name + "_maze_wf.png")

#=====

def export_json_to_file(name, json):
    file = open(name + ".json", 'w+')
    file.write(json)
    file.close()


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


random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 7))  


for x in range(0, 10):
    row = MAZE_WIDTH # random.randint(MAZE_WIDTH, int(MAZE_WIDTH * 1.5))
    col = MAZE_HEIGHT # random.randint(MAZE_HEIGHT, int(MAZE_HEIGHT * 1.5))
    aMAZEing = Maze(row, col, 0)
    aMAZEing.generate()
    aMAZEing.find_path()
    aMAZEing.add_door_randomly()
    aMAZEing.add_door_key_randomly()
    aMAZEing.add_entities_randomly()
    aMAZEing.add_non_interactive_objects()
    aMAZEing.add_interactive_objects()
    cells = aMAZEing.get_cells()
    draw_image(cells, row , col , "./maze_img/" + str(x)+ "_")
    draw_image_without_fill(cells, row , col , "./maze_img_wf/" + str(x)+ "_")
    export_json_to_file("./json_maps/map_"+str(x), aMAZEing.generate_map_json())
    export_json_to_file("./json_details/details_"+str(x), aMAZEing.generate_map_details_json(row, col))


# EoF
