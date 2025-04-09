import tkinter as tk
from tkinter import PhotoImage, messagebox
from PIL import Image, ImageTk

from screens import Screen
from game_state import my_screen_manager
from home_page import HomePageScreen

class SetUpCountryScreen(Screen):
    def __init__(self):
        super().__init__()

        # Heading label
        self.heading = tk.Label(self,
                                text="Set up your country",
                                font=('Arial', 30),
                                bg="white",
                                width=20,
                                height=2
                                )
        self.heading.pack(padx=10, pady=50)

        self.new_name = ""
        self.new_flag = ""
        self.valid_inputs = False

        # Name label
        self.name_heading = tk.Label(self, text="Name: ", font=('Arial', 20))
        self.name_heading.pack(padx=10, pady=10, anchor="w")

        # Text box for entering the name.
        self.name_box = tk.Entry(self, width=30, font=('Arial', 30))
        self.name_box.pack(padx=10, pady=40, anchor="w")

        # Label the section where the player choose the flag.
        self.flag_heading = tk.Label(self, text="Flag: ", font=('Arial', 20))
        self.flag_heading.pack(padx=10, pady=10, anchor="w")

        # Button to confirm choices.
        self.save_button = tk.Button(self, text="Save", font=('Arial', 20), command=self.save_choice)

        # paths
        self.flag_1 = "C:/Users\colet\OneDrive\Desktop\Computer science/NEA/flag_3.png"
        self.flag_2 = "C:/Users\colet\OneDrive\Desktop\Computer science/NEA/flag_3.png"
        self.flag_3 = "C:/Users\colet\OneDrive\Desktop\Computer science/NEA/flag_3.png"

        self.var = tk.IntVar()
        # Flag 1
        self.radio_button_1 = tk.Radiobutton(self,
                                 text="Flag 1",
                                 font=('Arial', 20),
                                 variable=self.var,
                                 value=1)
        self.radio_button_1.pack(padx=10, side="left")

        self.open_flag1 = Image.open(self.flag_1)
        self.flag1_photo_obj = ImageTk.PhotoImage(self.open_flag1)
        self.flag1_lbl = tk.Label(self, image = self.flag1_photo_obj)
        self.flag1_lbl.pack(padx=10, side="left")

        # Flag 2
        self.radio_button_2 = tk.Radiobutton(self,
                                  text="Flag 2",
                                  font=('Arial', 20),
                                  variable=self.var,
                                  value=2)
        self.radio_button_2.pack(padx=10, side="left")

        self.open_flag2 = Image.open(self.flag_2)
        self.flag2_photo_obj = ImageTk.PhotoImage(self.open_flag2)
        self.flag2_lbl = tk.Label(self, image = self.flag2_photo_obj)
        self.flag2_lbl.pack(padx=10, side="left")

        # Flag 3
        self.radio_button_3 = tk.Radiobutton(self,
                                 text="Flag 3",
                                 font=('Arial', 20),
                                 variable=self.var,
                                 value=3)
        self.radio_button_3.pack(padx=10, side="left")

        self.open_flag3 = Image.open(self.flag_3)
        self.flag3_photo_obj = ImageTk.PhotoImage(self.open_flag3)
        self.flag3_lbl = tk.Label(self, image = self.flag3_photo_obj)
        self.flag3_lbl.pack(padx=10, pady=10, side="left")

        self.save_button.pack()

    def verify_name(self):
        player_name = self.name_box.get()
        # length check is not needed as the length of the text box is the maximum length
        if player_name != "":
            # player_name can only have alphabets
            if player_name.isalpha():
                return True
        return False

    # invalid_message should be on the outside of the loop
    # make it an attribute
    # use a messagebox instead
    def set_name(self):
        if self.verify_name():
            valid_name = self.name_box.get()
            return valid_name
        else:
            return "Invalid name: name should only have alphabets." # instead of returning nothing

    def chose_flag(self):
        while self.var.get() != 0:
            # checking var to see what number it has changed to
            if self.var.get() == 1:
                new_flag = self.flag_1
            elif self.var.get() == 2:
                new_flag = self.flag_2
            else:
                new_flag = self.flag_3
            return new_flag

    # don't close unless all valid
    def save_choice(self):
        self.new_name = self.set_name()
        self.new_flag = self.chose_flag()
        if self.new_name == "Invalid name: name should only have alphabets.":
            self.show_error(self.new_name)
        else:
            self.destroy()
            self.valid_inputs = True
            setup_screen_object = my_screen_manager.get_screen_obj("my_setup")
            my_screen_manager.add_new("my_home", HomePageScreen(setup_screen_object.get_new_name(),
                                                                setup_screen_object.get_new_flag()))
            my_screen_manager.load_screen("my_home")


    def show_error(self, error_message):
        messagebox.showerror("Error", error_message)

    def get_new_name(self):
        if self.valid_inputs:
            return self.new_name
        else:
            return ""

    def get_new_flag(self):
        if self.valid_inputs:
            return self.new_flag
        else:
            return ""