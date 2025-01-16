import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Create window
window = tk.Tk()
window.geometry("1920x1080")
window.title("Country Simulation")

# Title
rgo_heading =  tk.Label(window,
                         text="Production",
                         font=('Arial', 30),
                         bg="white"
                         )
rgo_heading.pack(padx=10, pady=10, anchor="w")

# Products tabs
# Create notebook widget
tab_control = ttk.Notebook(window)


def make_tabs(tab_name, good_name, location, efficiency, firm_output, image_link):
    tab = ttk.Frame(tab_control)
    # Add tab name
    tab_control.add(tab, text=tab_name)
    tab_control.pack(expand=1, fill="both")

    # Image
    open_image = Image.open(image_link)
    product_photo = ImageTk.PhotoImage(open_image)
    product_photo_lbl = ttk.Label(window, image = product_photo)
    product_photo_lbl.pack(padx=10, side="right")

    # Labels for information of the firm

    ttk.Label(tab, text="Product: " + good_name, font=('Arial', 16)).pack(padx=10, pady=10, anchor="w")
    ttk.Label(tab, text="Location: " + location, font=('Arial', 16)).pack(padx=10, pady=10, anchor="w")
    ttk.Label(tab, text="Efficiency: " + efficiency, font=('Arial', 16)).pack(padx=10, pady=10, anchor="w")
    ttk.Label(tab, text="Output: " + firm_output, font=('Arial', 16)).pack(padx=10, pady=10, anchor="w")


window.mainloop()





