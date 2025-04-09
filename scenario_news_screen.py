import tkinter as tk
from tkinter import ttk
from screens import Screen
from tab_method import CreateNotebook

# # News screen to show the effect of the policy chosen.

class ScenarioNewsScreen(Screen):
    def __init__(self, news1, news2):
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

        self.news_lists = [news1, news2]

        self.my_note = CreateNotebook()
        self.my_note.add_tab('news1', "News 1", news1)
        self.my_note.add_tab('news2', 'News 2', news2)

