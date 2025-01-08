import tkinter as tk
from gettext import textdomain

from PIL import Image, ImageTk

# Initial country setup screen
# Create the window
window = tk.Tk()

# Provide the resolution and title of the window.
window.geometry("1920x1820")
window.title("Country Simulation")

# Show the heading
page_heading = tk.Label(window, text="Set up your country", font=('Arial', 30))
page_heading.pack(padx=10, pady=50)

# Label the text box for inputting the name of the country.
name_heading =  tk.Label(window, text="Name:", font=('Arial', 20))
name_heading.pack(padx=10, pady=10, anchor="w")

# The text box
name_tb = tk.Text(window, height=5, width=50)
name_tb.pack(padx=10, pady=10, anchor="w")

# Label section where the player chooses the flag.
flag_heading =  tk.Label(window, text="Flag:", font=('Arial', 20))
flag_heading.pack(padx=10, pady=10, anchor="w")

# Importing images
flag_image1 = Image.open("flag1.png")
flag_image2 = ImageTk.PhotoImage(flag_image1)

flag1_label = tk.Label(window,image = flag_image2)
flag1_label.pack()
window.mainloop()



