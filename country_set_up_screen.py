import tkinter as tk
from gettext import textdomain
from lib2to3.pygram import pattern_symbols
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Initial country setup screen
# Create the window
window = tk.Tk()

# Provide the resolution and title of the window.
window.geometry("1920x1080")
window.title("Country Simulation")

# Show the heading
page_heading = tk.Label(window,
                        text="Set up your country",
                        font=('Arial', 30),
                        bg="white",
                        width=20,
                        height=2
                        )
page_heading.pack(padx=10, pady=50)

# Label the text box for inputting the name of the country.
name_heading =  tk.Label(window,
                         text="Name:",
                         font=('Arial', 20)
                         )
name_heading.pack(padx=10, pady=10, anchor="w")

# The text box
name_tb = tk.Text(window,
                  height=1,
                  width=30,
                  font=('Arial', 30)
                  )
name_tb.pack(padx=10, pady=40, anchor="w")

# Label section where the player chooses the flag.
flag_heading =  tk.Label(window,
                         text="Flag:",
                         font=('Arial', 20)
                         )
flag_heading.pack(padx=10, pady=10, anchor="w")

# Importing images
# Flag 1
button1 = tk.Radiobutton(window,
                         text="Flag 1",
                         font=('Arial', 20))
button1.pack(padx=10, side="left")

open_flag1 = Image.open("C:/Users/colet/OneDrive/Desktop/flag1.png")
flag1_photo = ImageTk.PhotoImage(open_flag1)
flag1_lbl = tk.Label(window, image = flag1_photo)
flag1_lbl.pack(padx=10, side="left")

# Flag 2
button2 = tk.Radiobutton(window,
                          text="Flag 2",
                          font=('Arial', 20))
button2.pack(padx=10, side="left")

open_flag2 = Image.open("C:/Users/colet/OneDrive/Desktop/flag2.png")
flag2_photo = ImageTk.PhotoImage(open_flag2)
flag2_lbl = tk.Label(window, image = flag2_photo)
flag2_lbl.pack(padx=10, side="left")

# Flag 3
button3 = tk.Radiobutton(window,
                         text="Flag 3",
                         font=('Arial', 20))
button3.pack(padx=10, side="left")

open_flag3 = Image.open("C:/Users/colet/OneDrive/Desktop/flag3.png")
flag3_photo = ImageTk.PhotoImage(open_flag3)
flag3_lbl = tk.Label(window, image = flag3_photo)
flag3_lbl.pack(padx=10, pady=10, side="left")

window.mainloop()



