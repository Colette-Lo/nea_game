import tkinter as tk
from screens import Screen

# Where the context of the historical event is displayed.

class ScenarioInfoScreen(Screen):
    def __init__(self, context_name, context_info):
        super().__init__()
        self.title("Information Box")
        self.geometry("700x500")
        self.heading = tk.Label(self,
                                text="Context",
                                font=('Arial', 20),
                                bg="white",
                                width=20,
                                height=1
                                )
        self.heading.pack(padx=10, pady=30)
        self.context_title = tk.Label(self,
                                      text=context_name,
                                      font=('Arial', 20),
                                      bg="white",
                                      width=40,
                                      height=1
                                      )
        self.context_title.pack(padx=10)

        self.description = tk.Label(self,
                                    text=context_info,
                                    font=('Arial', 18),
                                    bg="white",
                                    width=40,
                                    height=20,
                                    wraplength=400
                                    )
        self.description.pack(padx=10, pady=30)


