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

        if (len(neigh) > 0):
            return neigh[random.randint(0,len(neigh)-1)]
        else:
            return None
        
