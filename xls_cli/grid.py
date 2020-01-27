import os
import math

class Grid:

    matrix = []
    selected = {"x": 0, "y": 0}
    pos = {"x": 0, "y": 0} 
    subgrid = []
    displacement = {"x": 0, "y": 0} 
    max_rows = 0
    max_cols = 0
    sheet = None

    def load_grid(self, sheet):
        self.sheet = sheet
        for rx in range(sheet.nrows):
            row = []
            for cx in range(sheet.ncols):
                row.append(sheet.cell_value(rowx=rx, colx=cx))
            self.matrix.append(row)
        self.calc_subgrid()

    def clear(self):
        self.subgrid = []
    
    def calc_subgrid(self):
        rows, columns = os.popen('stty size', 'r').read().split()
        rows, columns = int(rows), int(columns)

        self.max_rows = min(math.floor(rows/2), len(self.matrix)*2) - 2
        self.max_cols = min(int(math.floor(columns / 20)), len(self.matrix[0]))
        self.clear()

        max_pos_y = (self.max_rows - 1) + self.displacement["y"]
        max_pos_x = (self.max_cols - 1) + self.displacement["x"]
 
        for j in range(self.displacement["y"], min(max_pos_y, (self.sheet.nrows- 1))):
            self.subgrid.append(self.matrix[j][self.displacement["x"]:max_pos_x])

    def displace_x(self, increment):
        new_value = self.displacement["x"] + increment  

        if (new_value <= (self.max_cols - 1) and new_value >= 0):
            self.displacement["x"] = new_value
        self.calc_subgrid()

    def displace_y(self, increment):
        new_value = self.displacement["y"] + increment
        if (new_value < (len(self.matrix) - 1) and new_value > 0):
            self.displacement["y"] = new_value
        self.calc_subgrid()

    def move_right(self):
        new_pos_x = min(self.pos["x"] + 1, (self.max_cols-2))
        if new_pos_x == self.pos["x"]:
            self.displace_x(1) 
        self.pos["x"] = new_pos_x
        self.selected["x"] += 1
    
    def move_left(self):
        new_pos_x =  max(0, self.pos["x"] - 1)
        if new_pos_x == self.pos["x"]:
            self.displace_x(-1) 
        self.pos["x"] = new_pos_x
        self.selected["x"] -= 1
    
    def move_up(self): 
        new_pos_y = max(0, self.pos["y"] - 1)
        if new_pos_y == self.pos["y"]:
            self.displace_y(-1) 
        self.pos["y"] = new_pos_y
        self.selected["y"] -= 1

    def move_down(self):
        new_pos_y = min(self.pos["y"] + 1, (self.max_rows-2))
        if new_pos_y == self.pos["y"]:
            self.displace_y(1) 
        self.pos["y"] = new_pos_y
        self.selected["y"] += 1



        #if (self.selected["x"] > len(self.subgrid[0])):
        #    self.displace_sub_grid_left(len(self.subgrid[0]) - self.selected["x"])