import tkinter as tk
from tkinter import ttk
from tkinter import image_names
from screens import Screen

# # Country profile
# # Make the window
# window = tk.Tk()
# window.geometry("1920x1080")
# window.title("Country Simulation")
#
# # Window heading
# page_heading = tk.Label(window,
#                         text="Profile",
#                         font=('Arial', 30, "bold"),
#                         bg="white",
#                         width=10
#                         )
# page_heading.pack(padx=30, pady=30, anchor="w")
#
# # Flag
# # The procedure for displaying the chosen flag will be here
# # when the algorthm for user choosing a flag is added to the set-up screen later.
#
# # Name label
# name_heading =  tk.Label(window,
#                          text="Name: ",
#                          font=('Arial', 30),
#                          bg="white"
#                          )
# name_heading.pack(padx=10, pady=10, anchor="w")
#
# # Population label
# name_heading =  tk.Label(window,
#                          text="Population: ",
#                          font=('Arial', 30),
#                          bg="white"
#                          )
# name_heading.pack(padx=10, pady=10, anchor="w")
#
# # Table of metrics
# indicators = ['Life expectancy', 'Literacy rate', 'Happiness index', 'Inflation rate', 'Unemployment rate', 'GDP']
# data= ['', '', '', '', '', '']
# # data will be values for the indicators when calculations are implemented later.
#
# # Create the table, name the columns
# table = ttk.Treeview(window, columns=('Indicators', 'Values'), show='headings')
#
# # Add headings to the table
# table.heading('Indicators', text='Indicators')
# table.heading('Values', text='Values')
#
# table.pack(anchor='e', padx=100)
#
# # Insert values into the table
# for i in range(6):
#     indicator = indicators[i]
#     value = data[i]
#     table.insert(parent = '', index = 0, values = (indicator, value))
#
# window.mainloop()

class ProfileScreen(Screen):
    def __init__(self, name, population_size, indicators_values):
        super().__init__()
        self.heading = tk.Label(self,
                                text="Profile",
                                font=('Arial', 30),
                                bg="white",
                                width=10
                                )
        self.heading.pack(padx=30, pady=30, anchor="w")

        self.country_name =  tk.Label(self,
                                 text="Name: " + name,
                                 font=('Arial', 30),
                                 bg="white"
                                 )
        self.country_name.pack(padx=10, pady=10, anchor="w")

        self.pop_size =  tk.Label(self,
                                 text="Population: " + population_size,
                                 font=('Arial', 30),
                                 bg="white"
                                 )
        self.pop_size.pack(padx=10, pady=10, anchor="w")

        self.indicators = ['Life expectancy', 'Literacy rate', 'Happiness index', 'Inflation rate', 'Unemployment rate', 'GDP']
        self.values = indicators_values

        self.ind_table = ttk.Treeview(self,
                                      columns=('Indicators', 'Values'),
                                      show='headings'
                                      )

    def insert_values(self):
        self.ind_table.heading('Indicators', text='Indicators')
        self.ind_table.heading('Values', text='Values')

        self.ind_table.pack(anchor='e', padx=100)

        # Insert values into the table
        for i in range(6):
            indicator = self.indicators[i]
            value = self.values[i]
            self.ind_table.insert(parent = '', index = 0, values = (indicator, value))
