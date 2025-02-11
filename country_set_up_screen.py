import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

from screens import Screen

# # Initial country setup screen
# # Create the window
# window = tk.Tk()
#
# # Provide the resolution and title of the window.
# window.geometry("1920x1080")
# window.title("Country Simulation")
#
# # Show the heading
# page_heading = tk.Label(window,
#                         text="Set up your country",
#                         font=('Arial', 30),
#                         bg="white",
#                         width=20,
#                         height=2
#                         )
# page_heading.pack(padx=10, pady=50)
#
# # Label the text box for inputting the name of the country.
# name_heading =  tk.Label(window,
#                          text="Name:",
#                          font=('Arial', 20)
#                          )
# name_heading.pack(padx=10, pady=10, anchor="w")
#
# # The text box
# name_tb = tk.Text(window,
#                   height=1,
#                   width=30,
#                   font=('Arial', 30)
#                   )
# name_tb.pack(padx=10, pady=40, anchor="w")
#
# # Label section where the player chooses the flag.
# flag_heading =  tk.Label(window,
#                          text="Flag:",
#                          font=('Arial', 20)
#                          )
# flag_heading.pack(padx=10, pady=10, anchor="w")
#
# # Importing images
# # Flag 1
# button1 = tk.Radiobutton(window,
#                          text="Flag 1",
#                          font=('Arial', 20))
# button1.pack(padx=10, side="left")
#
# open_flag1 = Image.open("C:/Users/colet/OneDrive/Desktop/flag_1.png")
# flag1_photo = ImageTk.PhotoImage(open_flag1)
# flag1_lbl = tk.Label(window, image = flag1_photo)
# flag1_lbl.pack(padx=10, side="left")
#
# # Flag 2
# button2 = tk.Radiobutton(window,
#                           text="Flag 2",
#                           font=('Arial', 20))
# button2.pack(padx=10, side="left")
#
# open_flag2 = Image.open("C:/Users/colet/OneDrive/Desktop/flag_2.png")
# flag2_photo = ImageTk.PhotoImage(open_flag2)
# flag2_lbl = tk.Label(window, image = flag2_photo)
# flag2_lbl.pack(padx=10, side="left")
#
# # Flag 3
# button3 = tk.Radiobutton(window,
#                          text="Flag 3",
#                          font=('Arial', 20))
# button3.pack(padx=10, side="left")
#
# open_flag3 = Image.open("C:/Users/colet/OneDrive/Desktop/flag_3.png")
# flag3_photo = ImageTk.PhotoImage(open_flag3)
# flag3_lbl = tk.Label(window, image = flag3_photo)
# flag3_lbl.pack(padx=10, pady=10, side="left")
#
# window.mainloop()
#


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

        # Name label
        self.name_heading = tk.Label(self, text="Name: ", font=('Arial', 20))
        self.name_heading.pack(padx=10, pady=10, anchor="w")

        # Text box for typing in the name.
        self.name_box = tk.Entry(self, width=30, font=('Arial', 30))
        self.name_box.pack(padx=10, pady=40, anchor="w")

        # Label for the section where the player choose the flag.
        self.flag_heading = tk.Label(self, text="Flag: ", font=('Arial', 20))
        self.flag_heading.pack(padx=10, pady=10, anchor="w")

        # Flag options
        self.list_of_flags = [["Flag 1", "C:/Users/colet/OneDrive/Desktop/flag_1.png"],
                              ["Flag 2", "C:/Users/colet/OneDrive/Desktop/flag_2.png"],
                              ["Flag 3", "C:/Users/colet/OneDrive/Desktop/flag_3.png"]
                              ]
        self.radio_buttons = [["Flag 1"], ["Flag 2"], ["Flag 3"]]
        self.image_reference = []
        self.var = tk.StringVar()
        # Button to confirm choices.
        self.save_button = tk.Button(self, text="Save", font=('Arial', 20), command=self.save_choice)

        for i in range(len(self.list_of_flags)):
            # Open image
            open_flag = Image.open(self.list_of_flags[i][1])
            flag_photo = ImageTk.PhotoImage(open_flag)

            # Store image permanently.
            self.image_reference.append(flag_photo)

            # when the radiobutton is turned on by the player, variable is set to the current value option.
            # value can be returned in chose_flag().
            # use as the index of the flag in list of flags.
            # result: does not work.

            radio_btn = tk.Radiobutton(self,
                                       text=self.radio_buttons[i],
                                       image=self.image_reference[i],
                                       font=('Arial', 20),
                                       command=self.chose_flag(),
                                       variable=self.var,
                                       value=self.list_of_flags[i][0]
                                       )
            radio_btn.pack(padx=10, side="left")

            ## label for the images
            # flag_lbl = tk.Label(self, image=flag_photo)
            # flag_lbl.pack(padx=10, side="left")


    ### not needed. just use get().

    ## get name input by player
    # def get_name_input(self):
    #     return self.name_box.get()

    ###

    def verify_name(self):
        player_name = self.name_box.get()
        if player_name != "":
            if player_name.isalpha():
                return True
        return False


    def set_name(self):
        if self.verify_name():
            valid_name = self.name_box.get()
            return valid_name
        else:
            invalid_message = tk.Label(self, text="Name is not valid.", font=('Arial', 20))
            invalid_message.pack(padx=10, pady = 10, anchor="s")
            return ""

    ## error: var
    def chose_flag(self):
        print(self.var.get())
        chosen_flag_path = self.list_of_flags[int(self.var.get())]
        return chosen_flag_path

    def save_choice(self):
        new_name = self.set_name()
        new_flag_object = self.chose_flag()

        if new_name != "" and new_flag_object != "":
            return [new_name, new_flag_object]


tryscreen2 = SetUpCountryScreen()
tryscreen2.mainloop()