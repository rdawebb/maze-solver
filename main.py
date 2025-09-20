# import necessary modules
import logging
import time
from tkinter import Tk
from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

# configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# main function
def main():
    # create a window instance
    logging.info("Starting Maze Solver.")

    # log maze drawing start
    logging.info("Drawing maze...")

    # set maze parameters
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) // num_cols
    cell_size_y = (screen_y - 2 * margin) // num_rows
    window = Window(screen_x, screen_y)

    # create and draw a maze
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window)

    # log maze completion
    logging.info("Maze complete.")

    # change animation speed for solving
    maze.set_animate_speed(0.05)

    # wait for user input before solving
    logging.info("Press Space to solve the maze...")
    window.wait_for_key_press("space")

    # start timing the solve operation
    start_time = time.time()

    # log maze solving start
    logging.info("Solving maze...")

    # check if the maze is solved
    if maze.solve():
        # log successful solve and elapsed time
        elapsed_time = time.time() - start_time
        logging.info(f"Maze solved in {elapsed_time:.2f} seconds.")
    else:
        # log failure to solve and elapsed time
        elapsed_time = time.time() - start_time
        logging.warning(f"No solution found for the maze after {elapsed_time:.2f} seconds.")

    # wait for the window to close
    window.wait_for_close()

# entry point of the program
if __name__ == "__main__":
    main()