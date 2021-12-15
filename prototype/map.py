from cell import Cell

class Map():
    def __init__(self, rows, cols, c_w, c_h):
        self.rows = rows
        self.cols = cols
        self.c_w = c_w
        self.c_h = c_h
        self.cells = []

    def init_cells(self):
        for y in range(0, self.rows ):
            for x in range(0, self.cols ):
                self.cells.append(Cell(x, y , self.c_w, self.c_h ))
        
        return self.cells
    
    def index(self, x, y): #przerabia 2D na 1D list
        if (x < 0 or y < 0 or x > self.cols or y > self.rows):
            return None

        return x + y * self.cols 

    
    def generate_maze(self):
        current = self.cells[0] #our starting point, can be randomized later
        current.visited = True


        





