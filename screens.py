import tkinter as tk
from imghdr import tests
from tkinter import Image
from traceback import print_tb

from PIL import ImageTk


# Store all the screens
class MainApp(tk.Tk):# Using tk.Tk() as a parent class.
    def __init__(self):
        super.__init__() # Initialise the parent class, tk.Tk() which creates the window automatically.
        self.container = tk.Frame(self)
        self.frames = {}

    def show_frame(selfscreen):
        pass

# Basic attributes and methods for each screen.
class Screen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Country Simulation")
        self.geometry("1920x1080")
        self.heading = None

    def set_screen(self):
        pass

    def show_screen(self):
        pass

    def close_screen(self):
        pass

    def next_screen(self, screen_name):
        pass

