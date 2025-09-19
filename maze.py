# import necessary modules
import logging
import time
import random
from cell import Cell
from graphics import Point, Line

# configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# define the Maze class
class Maze:
  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None):
    self.__x1 = x1 # top-left x-coordinate of the maze
    self.__y1 = y1 # top-left y-coordinate of the maze
    self.__num_rows = num_rows # number of rows in the maze
    self.__num_cols = num_cols # number of columns in the maze
    self.__cell_size_x = cell_size_x # width of each cell
    self.__cell_size_y = cell_size_y # height of each cell
    self.__cells = [] # list to store the cells
    self.__window = window # reference to the window object

    self.__create_cells() # create the cells
    self.__break_entrance_and_exit() # break the entrance and exit walls

  # private method to create the cells
  def __create_cells(self):
    # create a 2D list of cells
    for col in range(self.__num_cols):
      # create a new column of cells
      col_cells = []
      for row in range(self.__num_rows):
        # create a new cell and add it to the column
        col_cells.append(Cell(self.__window))
      # add the column to the list of cells
      self.__cells.append(col_cells)

    # only draw cells if a window is provided
    if self.__window is not None:
      for col in range(self.__num_cols):
        for row in range(self.__num_rows):
          self.__draw_cell(col, row)

  # private method to draw a cell at a specific column and row
  def __draw_cell(self, col, row):

    # calculate the cell coordinates
    x1 = self.__x1 + col * self.__cell_size_x
    y1 = self.__y1 + row * self.__cell_size_y
    x2 = x1 + self.__cell_size_x
    y2 = y1 + self.__cell_size_y
    self.__cells[col][row].draw(x1, y1, x2, y2)

    # animate the drawing
    self.__animate()

  # private method to animate the drawing
  def __animate(self):
    # redraw the window if it exists
    if self.__window is None:
      return

    self.__window.redraw()
    time.sleep(0.05) # adjust the sleep time for speed control

  # private method to break the entrance and exit walls
  def __break_entrance_and_exit(self):
    # break the entrance wall (top-left cell)
    self.__cells[0][0].has_top_wall = False

    # only draw the cell if a window is provided
    if self.__window is not None:
      self.__draw_cell(0, 0)

    # break the exit wall (bottom-right cell)
    self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False

    # only draw the cell if a window is provided
    if self.__window is not None:
      self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)