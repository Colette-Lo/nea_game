import tkinter as tk
from tkinter import PhotoImage
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

class HomePageScreen(Screen):
    def __init__(self):
        super().__init__()
        self.prof_button = tk.Button(window,
                          text="Profile",
                          font=('Arial', 20),
                          width=10,
                          height=2
                          )

