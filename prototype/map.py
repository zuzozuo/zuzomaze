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



