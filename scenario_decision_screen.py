import tkinter as tk
from screens import Screen
from profile_screen import *
import random


# Scenario graph :)
# real_events_graph = {"The Great Famine of Ireland (1845-1852)": ["The Debt Crisis of the 1980s", "The Asian Financial Crisis (1997)"],
#                      "The Debt Crisis of the 1980s": ["The Bangladesh Garment Factory Collapse (2013)", "The Argentine Economic Crisis (1998-2002)"],
#                      "The Bangladesh Garment Factory Collapse (2013)": ["The Greek Debt Crisis (2009)"],
#                      "The Asian Financial Crisis (1997)":["The Argentine Economic Crisis (1998-2002)", "The Global Financial Crisis (2007-2008)"],
#                      "The Argentine Economic Crisis (1998-2002)": ["The Greek Debt Crisis (2009)", "The 1973 Oil Crisis"],
#                      "The Greek Debt Crisis (2009)": ["The Great Depression (1929)"],
#                      "The Great Depression (1929)": ["The Global Financial Crisis (2007-2008)"],
#                      "The Global Financial Crisis (2007-2008)": ["The 1973 Oil Crisis"],
#                      "The 1973 Oil Crisis": []
# }
#
# done_real_case = ["The Great Famine of Ireland (1845-1852)"]
#
# # loading events from json
# events_values = load_values('all_events.json')

class DecisionManager():
    def __init__(self):
        self.done_cases = ["The Great Famine of Ireland (1845-1852)"]


class ScenarioDecisionScreen(Screen):
    def __init__(self, content, op1, op2, op3):
        super().__init__()
        self.geometry("1300x650")
        self.heading = tk.Label(self,
                                text="Scenario",
                                font=('Arial', 20),
                                bg="white",
                                width=20,
                                height=1
                                )
        self.heading.pack(padx=10, pady=30)

        self.description = tk.Label(self,
                                    text=content,
                                    font=("Arial", 20),
                                    bg="white",
                                    height=7,
                                    width=45
                                    )
        self.description.pack(pady=10)

        self.option1 = tk.Label(self,
                               text=op1,
                               font=('Arial', 16),
                               bg="white",
                               height=10,
                               width=22)
        self.option1.pack(padx=10, side="left")

        self.option_button1 = tk.Radiobutton(self,
                         text="Option 1",
                         font=('Arial', 14))
        self.option_button1.pack(side="left")

        self.option2 = tk.Label(self,
                           text=op2,
                           font=('Arial', 16),
                           bg="white",
                           height=10,
                           width=22)
        self.option2.pack(padx=10, side="left")

        self.option_button2 = tk.Radiobutton(self,
                                             text="Option 2",
                                             font=('Arial', 14))
        self.option_button2.pack(side="left")

        self.option3 = tk.Label(self,
                           text=op3,
                           font=('Arial', 16),
                           bg="white",
                           height=10,
                           width=22)
        self.option3.pack(padx=10, side="left")

        self.option_button3 = tk.Radiobutton(self,
                                             text="Option 3",
                                             font=('Arial', 14))
        self.option_button3.pack(side="left")


        self.confirm_btn = tk.Button(self,
                                     text="Confirm",
                                     font=('Arial', 14),
                                     bg="white",
                                     )
        self.confirm_btn.pack()

    def click_confirm(self):
        pass

# Main
case_manager = DecisionManager()
# solve_case = ScenarioDecisionScreen("hello", "bye", "hi", "goodbye")
# solve_case.mainloop()