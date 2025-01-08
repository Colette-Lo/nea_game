import tkinter as tk
from tkinter import image_names


# Country profile
# Make the window
window = tk.Tk()
window.geometry("1920x1080")
window.title("Country Simulation")

# Window heading
page_heading = tk.Label(window,
                        text="Profile",
                        font=('Arial', 30, "bold"),
                        bg="white",
                        width=10
                        )
page_heading.pack(padx=30, pady=30, anchor="w")

# Flag
# country_flag = image file of the flag the player has selected
# country_flag = open image file
# flag_label = tk.Label(window, country_flag)
# flag_label.pack(anchor="w")

# Name label


window.mainloop()