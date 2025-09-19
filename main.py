# import necessary modules
import logging
from graphics import Window, Line, Point

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# main function
def main():
    # create a window instance
    logging.info("Starting the Maze Solver application.")
    window = Window(800, 600)

    # create some lines to draw
    line1 = Line(Point(100, 100), Point(200, 200))
    line2 = Line(Point(200, 100), Point(100, 200))

    # draw the lines on the window
    logging.info("Drawing lines.")
    window.draw_line(line1, "black")
    window.draw_line(line2, "black")

    # redraw the window to show the lines
    window.redraw()

    # wait for the window to close
    window.wait_for_close()

# entry point of the program
if __name__ == "__main__":
    main()