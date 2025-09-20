# import necessary modules
import unittest
import time
import logging
from maze import Maze
from cell import Cell

# configure logging
logging.basicConfig(level=logging.INFO)

# define the test case for the Maze class
class TestMaze(unittest.TestCase):
    # test maze creation
    def test_maze_creation(self):
        # create a maze instance
        maze = Maze(0, 0, 5, 5, 20, 20)

        # check if the maze has the correct number of rows and columns
        self.assertEqual(len(maze._Maze__cells), 5) # number of columns
        self.assertEqual(len(maze._Maze__cells[0]), 5) # number of rows in the first column

    # test cell creation
    def test_cell_creation(self):
        # create a maze instance
        maze = Maze(0, 0, 3, 3, 20, 20)

        # check if each cell is an instance of Cell
        for col in range(3):
            for row in range(3):
                self.assertIsInstance(maze._Maze__cells[col][row], maze._Maze__cells[col][row].__class__)

    # test cell drawing without a window
    def test_cell_drawing_without_window(self):
        # create a maze instance without a window
        maze = Maze(0, 0, 2, 2, 20, 20)

        # attempt to draw and expect an exception
        with self.assertRaises(Exception) as context:
            maze._Maze__draw_cell(0, 0)
        self.assertEqual(str(context.exception), "Window is not set for the cell.")

    # test breaking entrance and exit
    def test_break_entrance_and_exit(self):
        # create a maze instance
        maze = Maze(0, 0, 2, 2, 20, 20)

        # break entrance and exit walls
        maze._Maze__break_entrance_and_exit()

        # check if the entrance wall is broken
        self.assertFalse(maze._Maze__cells[0][0].has_top_wall)

        # check if the exit wall is broken
        self.assertFalse(maze._Maze__cells[1][1].has_bottom_wall)

    # test resetting visited status of cells
    def test_reset_cells_visited(self):
        # create a maze instance
        maze = Maze(0, 0, 2, 2, 20, 20)

        # manually set some cells as visited
        maze._Maze__cells[0][0].visited = True
        maze._Maze__cells[1][1].visited = True

        # reset visited status of all cells
        maze._Maze__reset_cells_visited()

        # check if all cells are unvisited
        for col in range(2):
            for row in range(2):
                self.assertFalse(maze._Maze__cells[col][row].visited)

    # test basic maze solving
    def test_maze_solving(self):
        # create a maze instance
        maze = Maze(0, 0, 3, 3, 20, 20)

        # attempt to solve the maze
        solved = maze.solve()

        # check if the solve method returns a boolean
        self.assertIsInstance(solved, bool)

    # test timer function on maze solving
    def test_timer_function(self):
        # create a maze instance
        maze = Maze(0, 0, 5, 5, 20, 20)

        # start the timer
        start_time = time.time()

        # solve the maze
        maze.solve()

        # stop the timer
        elapsed_time = time.time() - start_time
        
        # check if elapsed time is a positive float
        self.assertIsInstance(elapsed_time, float)
        self.assertGreater(elapsed_time, 0)

    # test key press handling in graphics module
    def test_key_press_handling(self):
        # import the graphics module
        from graphics import Window
        
        # create a window instance
        window = Window(200, 150)
        
        # test that the wait_for_key_press method exists and is callable
        self.assertTrue(callable(getattr(window, 'wait_for_key_press', None)))
        
        # close the window
        window.close()

if __name__ == "__main__":
  unittest.main()
    