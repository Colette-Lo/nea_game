import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from game_objects import good_list, prices, quantity_sold
from screens import Screen
from game_state import my_screen_manager
from country_set_up_screen import *
from scenario_decision_screen import load_scenario
from profile_screen import ProfileScreen
from trade_screen import TradeScreen
from technology_screen import TechnologyScreen
from production_screen import ProductionScreen
from budget_screen import BudgetScreen
from resource_gathering_screen import ResourceGatheringScreen

class HomePageScreen(Screen):
    def __init__(self, country_name, country_flag_path):
        super().__init__()

        self.country_name = country_name
        self.country_flag_path = country_flag_path

        # Using a frame as a menu bar.
        self.menu_frame = ttk.Frame(self)
        self.menu_frame.pack(side="top", fill="x", expand=False)

        my_screen_manager.add_new("my_profile", ProfileScreen, self.country_flag_path, self.country_name, 10000)
        my_screen_manager.add_new("my_trade", TradeScreen, good_list, prices, quantity_sold)
        my_screen_manager.add_new("my_tech", TechnologyScreen)
        my_screen_manager.add_new("my_prod", ProductionScreen)
        my_screen_manager.add_new("my_budget", BudgetScreen)
        my_screen_manager.add_new("my_resource", ResourceGatheringScreen)

        # Scenario button
        self.scenario_button = tk.Button(self,
                                         text="Scenarios",
                                         font=('Arial', 17),
                                         width=10,
                                         height=2,
                                         command=self.click_scenario
                                         )
        self.scenario_button.pack(anchor="w")

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

        map_lbl = tk.Label(self, image="C:/Users/colet/OneDrive/Desktop/game_map.png")
        map_lbl.pack(fill="x", expand=False)

    def click_scenario(self):
        load_scenario()

    def click_prof(self):
        my_screen_manager.load_screen("my_profile")

    def click_trade(self):
        my_screen_manager.load_screen("my_trade")

    def click_tech(self):
        my_screen_manager.load_screen("my_tech")

    def click_prod(self):
        my_screen_manager.load_screen("my_prod")

    def click_budget(self):
        my_screen_manager.load_screen("my_budget")

    def click_resource(self):
        my_screen_manager.load_screen("my_resource")