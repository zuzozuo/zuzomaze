import pygame

class Cell:
    def __init__(self, x, y, width, height):
        self.x = x #cols
        self.y = y #rows
        self.w = width
        self.h = height
        self.visited = False
        self.walls = [True, True, True, True] #top right bottom left



    