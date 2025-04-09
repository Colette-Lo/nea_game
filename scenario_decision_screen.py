import tkinter as tk
from game_state import my_screen_manager
from scenario_news_screen import ScenarioNewsScreen
from screens import Screen
from profile_screen import *
import random
from utilities import case_manager, choose_case, done_real_case, events_values, real_events_graph, levels
from scenario_news_screen import ScenarioNewsScreen
from scenario_info_screen import ScenarioInfoScreen

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

        self.var= tk.IntVar()

        self.option1 = tk.Label(self,
                               text=op1,
                               font=('Arial', 16),
                               bg="white",
                               height=10,
                               width=22,
                               )
        self.option1.pack(padx=10, side="left")

        self.option_button1 = tk.Radiobutton(self,
                         text="Option 1",
                         font=('Arial', 14),
                         variable=self.var,
                         value=1)
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
                                             font=('Arial', 14),
                                             variable=self.var,
                                             value=2)
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
                                             font=('Arial', 14),
                                             variable=self.var,
                                             value=3)
        self.option_button3.pack(side="left")


        self.confirm_btn = tk.Button(self,
                                     text="Confirm",
                                     font=('Arial', 14),
                                     bg="white",
                                     command=self.click_confirm
                                     )
        self.confirm_btn.pack()
        self.policy_chosen = False

    def chose_policy(self):
        while self.var.get() != 0:
            # checking var to see what number it has changed to
            if self.var.get() == 1:
                new_policy = "solution_1"
            elif self.var.get() == 2:
                new_policy = "solution_2"
            else:
                new_policy = "solution_3"
            return new_policy


    def click_confirm(self):
        self.destroy()
        self.policy_chosen = True

# Main

def load_scenario():
    # load scenario screen
    next_event_dict = choose_case(done_real_case, events_values, real_events_graph, levels)
    my_screen_manager.add_new("my_case", ScenarioDecisionScreen,
                              next_event_dict["event_description"],
                              next_event_dict["solution_options"]["solution_1"],
                              next_event_dict["solution_options"]["solution_2"],
                              next_event_dict["solution_options"]["solution_3"]
                              )

    # find the policy that has been chosen
    my_screen_manager.load_screen("my_case")
    scenario_screen_obj = my_screen_manager.get_screen_obj("my_case")
    chosen_solution = scenario_screen_obj.chose_policy()

    # load news screen
    case_news1 = next_event_dict["solution_options"][chosen_solution]["news"]["news1"]
    case_news2 = next_event_dict["solution_options"][chosen_solution]["news"]["news2"]
    my_screen_manager.add_new("my_news", ScenarioNewsScreen,case_news1,case_news2 )

    # load context screen if the case has context
    if next_event_dict["context"] is not None:
        my_screen_manager.add_new("my_context", ScenarioInfoScreen, next_event_dict["name"], next_event_dict["context"])
        my_screen_manager.load_screen("my_context")