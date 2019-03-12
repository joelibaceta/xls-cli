import os
import math

class Grid:

    matrix = []
    selected = {"x": 0, "y": 0}
    subgrid = []
    displace_x = 0
    displace_y = 0

    def load_grid(self, sheet):
        for rx in range(sheet.nrows):
            row = []
            for cx in range(sheet.ncols):
                row.append(sheet.cell_value(rowx=rx, colx=cx))
            self.matrix.append(row)
        self.load_subgrid()
    
    def load_subgrid(self):
        rows, columns = os.popen('stty size', 'r').read().split()
        rows, columns = int(rows), int(columns)
        max_rows = min(math.floor(rows/2), len(self.matrix)*2) - 2
        max_cols = min(int(math.floor(columns / 20)), len(self.matrix[0]))

        #for j in range(self.displace_y, max_rows + self.displace_y):
        #    self.subgrid[j].append(self.matrix[j][self.displace_x:max_cols + self.displace_x])

    def displace_sub_grid_left(self, n):
        self.displace_x = n
        self.load_subgrid()

    def displace_sub_grid_up(self, n):
        self.displace_y = n
        self.load_subgrid()

    def move_right(self):
        #if (self.selected["x"] > len(self.subgrid[0])):
        #    self.displace_sub_grid_left(len(self.subgrid[0]) - self.selected["x"])
        self.selected["x"] += 1
    
    def move_left(self):
        self.selected["x"] -= 1
    
    def move_up(self):
        #if (self.selected["y"] > len(self.subgrid)):
        #    self.displace_sub_grid_up(len(self.subgrid) - self.selected["y"])
        self.selected["y"] -= 1

    def move_down(self):
        self.selected["y"] += 1