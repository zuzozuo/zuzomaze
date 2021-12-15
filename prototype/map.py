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
    
    def index(self, x, y): #changes 2D list indexes into 1D list indexes
        if (x < 0 or y < 0 or x > self.cols-1 or y > self.rows-1):
            return None

        return x + y * self.cols 

    
    def removeWalls(self,c_a, c_b): #args of Cell type
        x = c_a.x - c_b.x #diffrence between x coords to check which wall to delete (right/left)
        y = c_a.y - c_b.y #diffrence between x coords to check which wall to delete (right/left)

        if (x == 1):
            c_a.removeLeftWall()
            c_b.removeRightWall()

        elif (x == -1):
            c_a.removeRightWall()
            c_b.removeLeftWall()

        if (y == 1):
            c_a.removeTopWall()
            c_b.removeBottomWall()
        elif (y == -1):
            c_a.removeBottomWall()
            c_b.removeTopWall()


        


        





