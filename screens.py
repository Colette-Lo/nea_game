import tkinter as tk

class Screen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Country Simulation")
        self.geometry("1920x1080")
        self.heading = None