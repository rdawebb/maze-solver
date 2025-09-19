# import necessary modules
import logging
from graphics import Window, Line, Point
from cell import Cell

# configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# main function
def main():
    # create a window instance
    logging.info("Starting the Maze Solver application.")
    window = Window(800, 600)

    # create and draw some cells

    logging.info("Drawing cells...")
    
    c = Cell(window)
    c.has_left_wall = False
    c.draw(100, 100, 200, 200)

    c = Cell(window)
    c.has_right_wall = False
    c.draw(200, 100, 300, 200)

    c = Cell(window)
    c.has_top_wall = False
    c.draw(300, 100, 400, 200)

    c = Cell(window)
    c.has_bottom_wall = False
    c.draw(400, 100, 500, 200)

    # wait for the window to close
    window.wait_for_close()

# entry point of the program
if __name__ == "__main__":
    main()