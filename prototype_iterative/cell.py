import pygame
import random

class Cell:
    def __init__(self, x, y, width, height):
        self.x = x #cols
        self.y = y #rows
        self.w = width
        self.h = height
        self.visited = False
        self.walls = [True, True, True, True] #top right bottom left
        self.isCurrent = False


    def checkNeighbors(self, top, right, bottom, left): #these are neighbouring cells
        neigh = []

        if (top is not None) and (not top.visited):
            neigh.append(top)

        if (right is not None) and (not right.visited):
            neigh.append(right)

        if (bottom is not None) and (not bottom.visited):
            neigh.append(bottom)
        
        if (left is not None) and (not left.visited):
            neigh.append(left)

        return neigh

    def removeTopWall(self):
        self.walls[0] = False
    
    def removeRightWall(self):
        self.walls[1] = False

    def removeBottomWall(self):
        self.walls[2] = False

    def removeLeftWall(self):
        self.walls[3] = False

        
