import tkinter as tk
from screens import Screen
from game_state import my_screen_manager
from country_set_up_screen import SetUpCountryScreen
from home_page import HomePageScreen

class StartScreen(Screen):
    def __init__(self):
        super().__init__()
        self.heading  = tk.Label(self,
                              text="Country Simulation",
                              font=('Arial', 40),
                              width=20,
                              height=2,
                              bg="white"
                              )
        self.heading.pack(padx=10, pady=200)

        self.is_first = True
        self.next_screen = ""

        self.start = tk.Button(self,
                         text="Start",
                         font=('Arial', 30),
                         width=10,
                         bg="white",
                         fg="red",
                         command=self.click_start
                         )
        self.start.pack()


    def click_start(self):
        if self.is_first:
            self.is_first = False
            self.load_setup()
        else:
            self.load_save()

    def load_setup(self):
        self.destroy()
        # self.next_screen = "my_setup"
        my_screen_manager.add_new("my_setup", SetUpCountryScreen)
        my_screen_manager.load_screen("my_setup")

    def load_save(self):
        self.destroy()
        # setup_screen_object = my_screen_manager.get_screen_obj("my_setup")
        # my_screen_manager.add_new("my_home", HomePageScreen(setup_screen_object.get_new_name(),
        #                                                     setup_screen_object.get_new_flag()))
        self.next_screen = "my_home"

    def get_next_screen(self):
        return self.next_screen


# my_screen_manager.add_new("my_setup", SetUpCountryScreen)