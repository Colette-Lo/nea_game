import tkinter as tk
from screens import Screen
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

        self.start = tk.Button(self,
                         text="Start",
                         font=('Arial', 30),
                         width=10,
                         bg="white",
                         fg="red",
                         command=self.click_start
                         )
        self.start.pack()

        self.is_first = True

    def click_start(self):
        if self.is_first:
            self.is_first = False
            self.load_setup()
            self.destroy()
            initial_setup_screen = SetUpCountryScreen()
            initial_setup_screen.mainloop()
        else:
            self.destroy()
            #load save from file
            home_page = HomePageScreen()
            home_page.mainloop()

    def load_setup(self):
        pass

    def load_save(self, ex_file):
        pass
