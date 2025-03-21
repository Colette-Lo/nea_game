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

# main
test_event = {
            "name": None,
            "event_description": "A major river just flooded yesterday, destroying many crops that were about to be harvested. There could be food shortages and rising prices for food in the coming months.",
            "context": None,
            "solution_options": [
                {
                    "solution_1": "Subsidize Food Imports: Reduce costs of essential food items.",
                    "food_supply": 0.5,
                    "price_level": -0.3,
                    "national_debt": 0.4
                },
                {
                    "solution_2": "Invest in Agricultural Subsidies: Increase local food production through support to farmers.",
                    "resource_gathering_efficiency": 0.4,
                    "GDP": 0.3,
                    "price_level": -0.1
                },
                {
                    "solution_3": "Enforce Price Controls: Set maximum price limits for staple foods to prevent exploitation.",
                    "price_level": -0.5,
                    "supply": -0.3,
                    "happiness_index": 0.2
                }
            ]
        }

def show_event_context(event_dict):
    if event_dict["name"] is not None:
        event_context_screen.mainloop()
    else:
        # for testing
        print("no context")

# testing calls
# give the event context to the screen
event_context_screen = ScenarioInfoScreen(test_event["name"], test_event["context"])
# call the procedure that determines if the window should show up
show_event_context(test_event)