import tkinter as tk
from tkinter import ttk, Frame


class CreateNotebook(ttk.Notebook):
    def __init__(self):
        ttk.Notebook.__init__(self) # Instantiate the object as a notebook.

    def add_tab(self, tab_name, text_title, content):
        new_tab = ttk.Frame(self)   # Use a frame to organise the widgets in the tab.

        # Add tab name
        self.add(new_tab, text=tab_name)
        self.pack(expand=1, fill="both")

        # Add tab title
        ttk.Label(new_tab, text=text_title, font=('Arial', 20)).grid(column=0,
                                                      row=0,
                                                      padx=30,
                                                      pady=30,
                                                      )
        # Add content
        ttk.Label(new_tab, text=content, font=('Arial', 16)).grid(column=0,
                                                 row=1,
                                                 padx=30,
                                                 pady=30
                                                 )
