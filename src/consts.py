#--------PYGAME CONSTS--------------------------------------------------
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

CELL_WIDTH = 100
CELL_HEIGHT = 100

MAZE_ROWS = (int)(WINDOW_WIDTH / CELL_WIDTH) #NUMBER OF CELLS IN ROW
MAZE_COLS = (int)(WINDOW_HEIGHT / CELL_HEIGHT) #NUMBER OF CELLS COLUMN


C_VISITED = (102, 170, 255)
C_VISITED_2 = (90, 10, 200)
C_BLUE  = (0, 0, 255)
C_WHITE = (255, 255, 255)
C_BLACK = (0,0,0)
C_ENDPOINT = (0, 230, 230)
C_NORMAL = (0,102,255)
BORDER_THICKNESS = 2

FONT_NAME = "Calibri"
#----------------------------------------------------------
# [GOAL START BFS_PATH IS_VISITED LEFT BOTTOM RIGHT TOP]
WALL_TOP         = 0b00000001
WALL_RIGHT       = 0b00000010
WALL_BOTTOM      = 0b00001000
WALL_LEFT        = 0b00001000

CELL_NOT_VISITED = 0b00000000
CELL_VISITED     = 0b00010000

CELL_BFS_PATH    = 0b00100000
CELL_IS_START    = 0b01000000
CELL_IS_GOAL     = 0b10000000