# import necessary modules
import logging
import time
from tkinter import Canvas, Tk, BOTH

# configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# define the Window class
class Window:
  def __init__(self, width, height):
    self.__root = Tk() # create the main window
    self.__root.title("Maze Solver") # set the window title
    self.__canvas = Canvas(self.__root, width=width, height=height, bg="white") # create a canvas
    self.__canvas.pack(fill=BOTH, expand=1) # pack the canvas to fill the window
    self.__running = False # flag to control the main loop
    self.__root.protocol("WM_DELETE_WINDOW", self.close) # handle window close event
    self.__key_pressed = False # flag to track key press
    self.__root.focus_set() # ensure the window can receive key events

  # method to redraw the canvas
  def redraw(self):
    # update the canvas
    self.__canvas.update_idletasks()
    self.__canvas.update()

  # method to wait for the window to close
  def wait_for_close(self):
    # start the main loop
    self.__running = True
    while self.__running:
      # handle events and update the window
      try:
        # update the window
        self.__root.update_idletasks()
        self.__root.update()
      
      # catch exceptions to handle window closure
      except Exception as e:
        logging.error(f"Error occurred: {e}")

        # handle window closure
        self.__running = False

  # method to draw a line on the canvas
  def draw_line(self, line, fill_colour="black"):
    # draw a line on the canvas
    line.draw(self.__canvas, fill_colour)

  # method to wait for a specific key press
  def wait_for_key_press(self, key="space", wait_time=10):
    # reset the key pressed flag
    self.__key_pressed = False
    
    # key press event handler
    def on_key_press(event):
      if event.keysym.lower() == key.lower():
        self.__key_pressed = True
    
    # bind the key press event
    self.__root.bind("<KeyPress>", on_key_press)
    
    # record the start time
    start_time = time.time()
    warning_shown = False

    # wait for the key to be pressed (using a simple condition instead of __running)
    while not self.__key_pressed:
      try:
        self.__root.update_idletasks()
        self.__root.update()
        
        # small delay to prevent excessive CPU usage
        time.sleep(0.01)

        # check for inactivity and warn the user (only once)
        if not warning_shown and time.time() - start_time >= wait_time:
          logging.info(f"No key press detected after {wait_time} seconds, are you still there?")
          warning_shown = True

        # check for inactivity and exit if necessary
        if time.time() - start_time >= wait_time * 2:
          logging.info(f"No key press detected after {wait_time * 2} seconds of inactivity.")
          break

      except Exception as e:
        logging.error(f"Error occurred while waiting for key press: {e}")
        break
    
    # unbind the key press event
    self.__root.unbind("<KeyPress>")

  # method to close the window
  def close(self):
    # log the window closure
    logging.info("Closing window.")

    # set the running flag to false to exit the main loop
    self.__running = False

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Line:
  def __init__(self, point1, point2):
    self.point1 = point1
    self.point2 = point2

  def draw(self, canvas, fill_colour="black"):
    canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_colour, width=2)