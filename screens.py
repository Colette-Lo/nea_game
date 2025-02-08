import tkinter as tk

# Store all the screens
# class MainApp(tk.Tk):# Using tk.Tk() as a parent class.
#     def __init__(self):
#         super.__init__() # Initialise the parent class, tk.Tk() which creates the window automatically.
#         self.container = tk.Frame(self)
#         self.frames = {}
#
#     def show_frame(self, screen):
#         pass

## Solution for changing screens:
## store screens using a tree
## use traversal algorithms to track what screens have been opened
## possibly a stack to pop back to the previous screens.
## task for milestone 2

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

