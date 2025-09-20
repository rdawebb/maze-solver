# import necessary modules
import logging
from graphics import Point, Line

# configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# define the Cell class
class Cell:
    # initialize the cell with walls and position
    def __init__(self, window=None, visited=False):
        self.has_right_wall = True # right wall exists
        self.has_left_wall = True # left wall exists
        self.has_top_wall = True # top wall exists
        self.has_bottom_wall = True # bottom wall exists
        self.__x1 = -1 # top-left x-coordinate
        self.__y1 = -1 # top-left y-coordinate
        self.__x2 = -1 # bottom-right x-coordinate
        self.__y2 = -1 # bottom-right y-coordinate
        self.window = window # reference to the window object
        self.visited = visited # flag to indicate if the cell has been visited

    # method to draw the cell on the window
    def draw(self, x1, y1, x2, y2):
        # ensure the window is set
        if self.window is None:
            # raise an error if the window is not set
            raise ValueError("Window is not set for the cell.")

        # store the cell coordinates
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        # check if right wall exists and draw it
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.window.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.window.draw_line(line, "white")

        # check if left wall exists and draw it
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.window.draw_line(line, "white")

        # check if top wall exists and draw it
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.window.draw_line(line, "white")
        
        # check if bottom wall exists and draw it
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.window.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.window.draw_line(line, "white")

    # method to draw a move from this cell to another cell
    def draw_move(self, to_cell, undo=False):
        # if no window is set, skip drawing for testing purposes
        if self.window is None:
            return

        # ensure the target cell is set
        if to_cell is None or not isinstance(to_cell, Cell):
            # raise an error if the target cell is not set
            raise ValueError("Target cell is not set for the move or is not a Cell instance.")
        
        # calculate centre point of first cell
        x_centre = (self.__x1 + self.__x2) / 2
        y_centre = (self.__y1 + self.__y2) / 2

        # calculate centre point of second cell
        x_centre2 = (to_cell.__x1 + to_cell.__x2) / 2
        y_centre2 = (to_cell.__y1 + to_cell.__y2) / 2

        # determine the line colour based on whether it's an undo move
        fill_colour = "red" if not undo else "grey"

        # create a line between the two centre points
        line = Line(Point(x_centre, y_centre), Point(x_centre2, y_centre2))

        # draw the line on the window
        self.window.draw_line(line, fill_colour)