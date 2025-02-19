import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from screens import Screen

# # Create window
# window = tk.Tk()
# window.geometry("1920x1080")
# window.title("Country Simulation")
#
# # Profile button
# profile_button = tk.Button(window,
#                          text="Profile",
#                          font=('Arial', 20),
#                          width=10,
#                          height=2
#                          )
# profile_button.pack(anchor='w')
#
# # Menu bar
# menu_bar = tk.Frame(window)
# menu_bar.columnconfigure(0, weight=1) # One line for one column.
#
# # Add items to the menu bar as buttons.
# resources_btn = tk.Button(menu_bar,
#                           text="Resources",
#                           font=('Arial', 17),
#                           width=15,
#                           height=2
#                           )
# resources_btn.grid(row=0,
#                    column=0,
#                    sticky=tk.W+tk.E
#                    )
#
# tp_btn = tk.Button(menu_bar,
#                    text="Trade & Production",
#                    font=('Arial', 17),
#                    width=15,
#                    height=2
#                    )
# tp_btn.grid(row=0,
#             column=1,
#             sticky=tk.W+tk.E
#             )
#
# tech_btn = tk.Button(menu_bar,
#                      text="Technology",
#                      font=('Arial', 17),
#                      width=15,
#                      height=2
#                      )
# tech_btn.grid(row=0,
#               column=2,
#               sticky=tk.W+tk.E
#               )
#
# firms_btn = tk.Button(menu_bar,
#                       text="Firms",
#                       font=('Arial', 17),
#                       width=15,
#                       height=2
#                       )
# firms_btn.grid(row=0,
#                column=3,
#                sticky=tk.W+tk.E
#                )
#
# budget_btn = tk.Button(menu_bar,
#                        text="Budget",
#                        font=('Arial', 17),
#                        width=15,
#                        height=2
#                        )
# budget_btn.grid(row=0,
#                 column=4,
#                 sticky=tk.W+tk.E
#                 )
#
# rgo_btn = tk.Button(menu_bar,
#                     text="Resource gathering",
#                     font=('Arial', 17),
#                     width=15,
#                     height=2
#                     )
# rgo_btn.grid(row=0,
#              column=5,
#              sticky=tk.W+tk.E
#              )
#
# menu_bar.pack()
#
# # Scenario button
# scenarios_button = tk.Button(window,
#                          text="Scenarios",
#                          font=('Arial', 20),
#                          width=10,
#                          height=2
#                          )
# scenarios_button.pack(anchor='w')
#
# # Display map
# open_map = Image.open("C:/Users/colet/OneDrive/Desktop/game_map.png")
# map_file = ImageTk.PhotoImage(open_map)
# map_lbl = tk.Label(window, image = map_file)
# map_lbl.pack(fill='both', expand=True)
#
# window.mainloop()

# def alt_make_menu(self):
#     # Add items to the menu bar as buttons.
#     resources_btn = tk.Button(self.menu_frame, text="Resources", font=('Arial', 17), width=15, height=2)
#     resources_btn.grid(row=0, column=0, sticky=tk.W + tk.E)
#
#     tp_btn = tk.Button(self.menu_frame, text="Trade & Production", font=('Arial', 17), width=15, height=2)
#     tp_btn.grid(row=0, column=1, sticky=tk.W + tk.E)
#
#     tech_btn = tk.Button(self.menu_frame, text="Technology", font=('Arial', 17), width=15, height=2)
#     tech_btn.grid(row=0, column=2, sticky=tk.W + tk.E)
#
#     firms_btn = tk.Button(self.menu_frame, text="Firms", font=('Arial', 17), width=15, height=2)
#     firms_btn.grid(row=0, column=3, sticky=tk.W + tk.E)
#
#     budget_btn = tk.Button(self.menu_frame, text="Budget", font=('Arial', 17), width=15, height=2)
#     budget_btn.grid(row=0, column=4, sticky=tk.W + tk.E)
#
#     rgo_btn = tk.Button(self.menu_frame, text="Resource gathering", font=('Arial', 17), width=15, height=2)
#     rgo_btn.grid(row=0, column=5, sticky=tk.W + tk.E)

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
                                         height=2
                                         )
        self.scenario_button.pack(anchor="w")

        #List of instances from each screen class.
        self.menu_items = ["Profile", "Trade", "Technology", "Production", "Budget", "Resource gathering"]
        self.show_menu()

        # Map image
        self.map_image_path = "C:/Users/colet/OneDrive/Desktop/game_map.png"
        self.map_opened = []
        self.show_map()

    def show_map(self):
        open_map = Image.open(self.map_image_path)
        map_file = ImageTk.PhotoImage(open_map)

        self.map_opened.append(map_file)

        map_lbl = tk.Label(self, image=map_file)
        map_lbl.pack(fill="x", expand=False)

    def make_menu_button(self, item, grid_num):
        tk.Button(self.menu_frame, text=item, font=('Arial', 17), width=15, height=2).grid(row=0, column=grid_num)

    def show_menu(self):
        for i in range(len(self.menu_items)):
            self.make_menu_button(self.menu_items[i], i)

    def click_scenario(self):
        pass

    def click_menu(self):
        pass








### tested. ####
## made an alternative method for the menu bar just in case ##
##### CHANGE SCREENSHOTS FOR MILESTONE 1
##### THERE IS NO RESOURCE SCREEN WHY DID YOU ADD RESOURCES TO THE LIST
##### THERE IS ALSO NO FIRMS. JUST TRADE, AND PRODUCTION. THEY ARE SEPARATED.
