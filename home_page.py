import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from screens import Screen
from profile_screen import ProfileScreen
from trade_screen import TradeScreen
from technology_screen import TechnologyScreen
from production_screen import ProductionScreen
from budget_screen import BudgetScreen
from resource_gathering_screen import ResourceGatheringScreen

class HomePageScreen(Screen):
    def __init__(self):
        super().__init__()

        # Using a frame as a menu bar.
        self.menu_frame = ttk.Frame(self)
        self.menu_frame.pack(side="top", fill="x", expand=False)

        # Scenario button
        self.scenario_button = tk.Button(self,
                                         text="Scenarios",
                                         font=('Arial', 17),
                                         width=10,
                                         height=2,
                                         command=self.click_scenario
                                         )
        self.scenario_button.pack(anchor="w")

        #List of instances from each screen class.
        # self.menu_items = ["Profile", "Trade", "Technology", "Production", "Budget", "Resource gathering"]
        # self.show_menu()

        # Map image
        self.map_image_path = "C:/Users/colet/OneDrive/Desktop/game_map.png"
        self.map_opened = []
        self.show_map()

        self.var = tk.IntVar()
        # Menu buttons
        self.prof_btn = tk.Button(self.menu_frame, text="Profile", font=('Arial', 17), width=19, height=2, command=self.click_prof)
        self.prof_btn.grid(row=0, column=0)

        self.trade_btn = tk.Button(self.menu_frame, text="Trade", font=('Arial', 17), width=19, height=2, command=self.click_trade)
        self.trade_btn.grid(row=0, column=1)

        self.tech_btn = tk.Button(self.menu_frame, text="Technology", font=('Arial', 17), width=19, height=2, command=self.click_tech)
        self.tech_btn.grid(row=0, column=2)

        self.prod_btn = tk.Button(self.menu_frame, text="Production", font=('Arial', 17), width=19, height=2, command=self.click_prod)
        self.prod_btn.grid(row=0, column=3)

        self.budget_btn = tk.Button(self.menu_frame, text="Budget", font=('Arial', 17), width=19, height=2, command=self.click_budget)
        self.budget_btn.grid(row=0, column=4)

        self.resource_btn = tk.Button(self.menu_frame, text="Resource Gathering", font=('Arial', 17), width=19, height=2, command=self.click_resource)
        self.resource_btn.grid(row=0, column=5)

    def show_map(self):
        open_map = Image.open(self.map_image_path)
        map_file = ImageTk.PhotoImage(open_map)

        self.map_opened.append(map_file)

        map_lbl = tk.Label(self, image=map_file)
        map_lbl.pack(fill="x", expand=False)

    # def make_menu_button(self, item, grid_num):
    #     tk.Button(self.menu_frame, text=item, font=('Arial', 17), width=15, height=2).grid(row=0, column=grid_num)

    # def show_menu(self):
    #     for i in range(len(self.menu_items)):
    #         self.make_menu_button(self.menu_items[i], i)

    def click_scenario(self):
        pass

    def click_prof(self):
        prof_screen = ProfileScreen("nhk", "C:/Users/colet/OneDrive/Desktop/flag_1.png", "12345", [12, 123, 1234, 123, 1234, 1234])

    def click_trade(self):
        trad_screen = TradeScreen([], [], [])

    def click_tech(self):
        tech_screen = TechnologyScreen()

    def click_prod(self):
        prod_screen = ProductionScreen()

    def click_budget(self):
        budg_screen = BudgetScreen("123", "456", "789")

    def click_resource(self):
        rgo_screen = ResourceGatheringScreen()


### tested. ####
## made an alternative method for the menu bar just in case ##
##### CHANGE SCREENSHOTS FOR MILESTONE 1
##### NO RESOURCE SCREEN
##### ALSO NO FIRMS. JUST TRADE, AND PRODUCTION. THEY ARE SEPARATED.
# try_home = HomePageScreen()
# try_home.mainloop()