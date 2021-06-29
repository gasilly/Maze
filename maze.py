import random
import sys

class Maze:
    def __init__(self,_height,_width):
        sys.setrecursionlimit(3000)
        self.width = _width
        self.height = _height
        self.grid = [[0b1111] * self.width for i in range(self.height)]

    def displayGrid(self): #display the current maze state where every binary value represents a wall N-S-W-E
        print()
        for r in self.grid:
            for c in r:
                print(format(c, '#06b'), end=' ')
            print()

    def setHeight(self,_height):
        self.height = _height

    def setWidth(self,_width):
        self.width = _width

    def resetGrid(self):
        self.grid = [[0b1111] * self.width for i in range(self.height)]

    def recursiveAlgorithm(self, current_position): #use a recursive algorithm to create the maze
        not_checked_position = [0,1,2,3]
        opposite_wall_key = {3:2,2:3,1:0,0:1}
        new_grid_direction = [0,0]
        while True: #Pick a valid direction
            newposition = random.choice(not_checked_position) #get a new direction and remove both its bit and the opposite in the next tile
            not_checked_position.remove(newposition)
            if (newposition == 3 and (current_position[0] - 1) >= 0) and self.grid[max(0,current_position[0] - 1)][current_position[1]] == 0b1111: # Upward direction
                    new_grid_direction[0] = -1
                    opposite_wall = 2
            elif (newposition == 2 and ((current_position[0] + 1) < self.height)) and (self.grid[min(self.height - 1,current_position[0] + 1)][current_position[1]] == 0b1111): # Downward direction
                    new_grid_direction[0] = 1
                    opposite_wall = 3
            elif (newposition == 1 and (current_position[1] - 1) >= 0) and self.grid[current_position[0]][max(0,current_position[1] - 1)] == 0b1111: # Left direction
                    new_grid_direction[1] = -1
                    opposite_wall = 0
            elif (newposition == 0 and ((current_position[1] + 1) < self.width)) and self.grid[current_position[0]][min(self.width - 1,current_position[1] + 1)] == 0b1111: # Right direction
                    new_grid_direction[1] = 1
                    opposite_wall = 1

            if (new_grid_direction[0] != 0) or (new_grid_direction[1] != 0): #Bit Manipulation
                self.grid[current_position[0]][current_position[1]] = self.grid[current_position[0]][current_position[1]] ^ (1 << newposition)
                self.grid[current_position[0] + new_grid_direction[0]][current_position[1] + new_grid_direction[1]] = self.grid[current_position[0] + new_grid_direction[0]][current_position[1] + new_grid_direction[1]] ^ (1 << opposite_wall)
                self.recursiveAlgorithm([current_position[0] + new_grid_direction[0], current_position[1] + new_grid_direction[1]])
                new_grid_direction = [0,0]

            if len(not_checked_position) == 0:
                break

    def drawSolution(self):
        return