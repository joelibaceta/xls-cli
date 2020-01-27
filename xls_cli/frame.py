import os

import math
import xls_cli.ansi as ansi
from xls_cli.grid import Grid
from getkey import getkey, keys

class Frame:

    width, height = 0, 0
    printable_window = "\x1B[2J" 
    title = "unititled"
    grid = None

    def __init__(self, title):
        rows, columns = os.popen('stty size', 'r').read().split()
        self.title = title
        self.height = int(rows)
        self.width = int(columns)
    
    def render(self):
        self.printable_window += self.draw_title_bar()
        self.printable_window += self.draw_grid() 
        print(self.printable_window)
    
    def loop(self):
        while 1:    
            key = getkey()
            if key == keys.UP:
                self.grid.move_up()
                self.refresh()
            if key == keys.DOWN:
                self.grid.move_down()
                self.refresh()
            if key == keys.RIGHT:
                self.grid.move_right()
                self.refresh()
            if key == keys.LEFT:
                self.grid.move_left()
                self.refresh()
            elif key == 'q':
                quit()

    def refresh(self):
        self.printable_window = "\x1B[2J"
        self.render()

    def draw_title_bar(self):
        title = "%s - %s" %("xls-cli", self.title)
        return ansi.bg(title.center(self.width, " "), 28)

    def draw_grid(self):

        grid_to_string = "\n" + "-" * self.width + "\n"

        for j in range(0, (len(self.grid.subgrid))):
            row = []
            for i in range(0, (len(self.grid.subgrid[0]) )):
                
                text = "{:<20}".format(" " + str(self.grid.subgrid[j][i]))

                if (j == self.grid.pos["y"] and i == self.grid.pos["x"]):
                    text = ansi.bg(text, 8)
                row.append(text)
                
            line_separator = "-" * self.width
            grid_to_string += "%s\n%s\n" %("|".join(row), line_separator)
        

        
        #grid_to_string += max(0, (self.grid.sheet.nrows - self.grid.max_rows)) * "\n"

        return grid_to_string
     