import xlrd
from xls_cli.frame import Frame 
from xls_cli.grid import Grid

class Runner:
    
    def open_file(file_path):
        frame = None
        book = xlrd.open_workbook(file_path)
        sh = book.sheet_by_index(0)
        grid = Grid()
        grid.load_grid(sh)
        frame = Frame(file_path)
        frame.grid = grid
        frame.render()
        frame.loop()    