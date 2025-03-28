import tkinter as tk
from tkinter import ttk
from screens import Screen
from tab_method import CreateNotebook

# # News screen to show the effect of the policy chosen.

class ScenarioNewsScreen(Screen):
    def __init__(self):
        super().__init__()
        self.heading = tk.Label(self,
                                text="News",
                                font=('Arial', 20),
                                bg="white",
                                width=20,
                                height=1
                                )
        self.heading.pack(padx=10, pady=20)

        self.geometry("700x500")

        self.news_lists = []
        # this list will be filled with all the news for all possible scenarios.

        self.trynote = CreateNotebook()
        self.trynote.add_tab('news1', "Example title", "Example content")
        self.trynote.add_tab('news2', 'hi', "idk")

trynewsscreen = ScenarioNewsScreen()
trynewsscreen.mainloop()
