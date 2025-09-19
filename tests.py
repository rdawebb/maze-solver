# import necessary modules
import unittest
from maze import Maze
from cell import Cell

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

if __name__ == "__main__":
  unittest.main()
    