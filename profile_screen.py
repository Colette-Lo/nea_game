import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from screens import Screen

# # Country profile
class LevelManager():
    def __init__(self):
        # ADD TO REPORT
        # determining the level of development
        self.level = 1
        self.gdp_value = tryscreen.values[-1]
        self.change_level()

        # ADD TO REPORT
        # determining the level of development
    def change_level(self):
        if self.gdp_value <= 1135.0:
            self.level = 1
        elif 1135.0 < self.gdp_value <= 13845.0:
            self.level = 2
        else:
            self.level = 3

class ProfileScreen(Screen):
    def __init__(self, name, flag_path, population_size):
        super().__init__()
        self.heading = tk.Label(self,
                                text="Profile",
                                font=('Arial', 30),
                                bg="white",
                                width=10
                                )
        self.heading.pack(padx=30, pady=30, anchor="w")

        # indicators table
        self.indicators = ['Life expectancy (years)', 'Literacy rate (%)', 'Happiness index (0-10)', 'Inflation rate (%)', 'Unemployment rate (%)',
                           'GDP (£)']
        self.values = [30.0, 1, 1, 1, 7, 100]

        self.ind_table = ttk.Treeview(self,
                                      columns=('Indicators', 'Values'),
                                      show='headings',
                                      height = 6
                                      )
        self.insert_values()

        # flag
        self.flag_image_path = flag_path
        self.keep_flag = []
        self.show_flag()

        # country name
        self.country_name = tk.Label(self,
                                     text="Name: " + name,
                                     font=('Arial', 40),
                                     bg="white"
                                     )
        self.country_name.pack(padx = 10, pady = 10, anchor="w")

        # population
        self.pop_size =  tk.Label(self,
                                 text="Population: " + population_size,
                                 font=('Arial', 40),
                                 bg="white"
                                 )
        self.pop_size.pack(padx = 10, pady = 10, anchor="w")

    # Display flag.
    # Need to add method to class diagram for ProfileScreen.
    def show_flag(self):
        open_flag = Image.open(self.flag_image_path)
        flag_file = ImageTk.PhotoImage(open_flag)

        self.keep_flag.append(flag_file)

        flag_lbl = tk.Label(self, image=flag_file, width = 400, height = 400)
        flag_lbl.pack(expand=False, anchor="w")
    ## have not tested ##

    def insert_values(self):
        self.ind_table.heading('Indicators', text='Indicators')
        self.ind_table.heading('Values', text='Values')

        self.ind_table.pack(side=tk.RIGHT, padx = 20, fill = 'x')

        # Insert values into the table
        for i in range(6):
            self.ind_table.insert(parent = '', index = 0, values = (self.indicators[i], self.values[i]))


    def cal_gdp(self, scale):
        # the limit for GDP is >0
        if scale >= -1:
            # store the current value
            original = self.values[5]
            # calculate the new value
            new = original * (1+scale)
        else:
            new = 0
        # update the value to be display as the GDP
        self.values[5] = new
        # a print statement for testing
        # print("GDP:",self.values[5])

    def cal_unemployment(self, scale):
        # the limit for unemployment rate is 0% to 100%
        if 0<= self.values[4] <= 100:
            # store the current value
            original = self.values[4]
            # calculate the new value
            new = original + scale
            # checking if the new value is still within the range
            if 0 <= new <= 100:
                self.values[4] = new
            elif new < 0:
                self.values[4] = 0
            else:
                self.values[4] = 100
        # a print statement for testing
        # print("Unemployment:", self.values[4])

    def cal_inflation(self, scale):
        # store the current value
        original = self.values[3]
        # calculate the new value
        new = original + scale
        # update the value to be display as the inflation rate
        self.values[3] = new
        # a print statement for testing
        # print("Inflation", self.values[3])

    def cal_happiness(self, scale):
        # the limit for the happiness index is 0 to 10
        if 0<= self.values[2] <=10:
            # store the current value
            original = self.values[2]
            # calculate the new value
            new = original * (1+scale)
            # checking if the new value is still within the range
            if 0 <= new <= 10:
                self.values[2] = new
            elif new < 0:
                self.values[2] = 0
            else:
                self.values[2] = 10
        # a print statement for testing
        # print("Happiness index:", self.values[2])

    def cal_literacy(self, scale):
        # the limit for literacy is 0% to 100%
        if 0<= self.values[1] <= 100:
            # store the current value
            original = self.values[1]
            # calculate the new value
            new = original + scale
            # checking if the new value is still within the range
            if 0 <= new <= 100:
                self.values[1] = new
            elif new < 0:
                self.values[1] = 0
            else:
                self.values[1] = 100
        # a print statement for testing
        # print("Literacy rate", self.values[1])

    def cal_life_expectancy(self, scale):
        # the minimum age is 0 years old
        if 0<= self.values[0]:
            # store the current value
            original = self.values[0]
            # calculate the new value
            new = original * (1+scale)
            rounded_new = round(new, 1)
            # checking if the new value is still within the range
            if 0 < new:
                self.values[0] = rounded_new
            else:
                self.values[0] = 0.5
        # a print statement for testing
        # print("Life expectancy:", self.values[0])

# , [12, 123, 1234, 123, 1234, 1234]
tryscreen = ProfileScreen("nhk", "C:/Users/colet/OneDrive/Desktop/flag_1.png", "12345")

tryscreen.mainloop()