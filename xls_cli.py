import xlrd
from frame import Frame 
from grid import Grid

class XlsCli:

    frame = None
    
    def open_file(self, file_path):
        book = xlrd.open_workbook(file_path)
        sh = book.sheet_by_index(0)
        grid = Grid()
        grid.load_grid(sh)
        self.frame = Frame(file_path)
        self.frame.grid = grid

    def render(self):
        self.frame.render()
        self.frame.loop()