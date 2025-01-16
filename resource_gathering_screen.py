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
                         text="Resource gathering operations",
                         font=('Arial', 30),
                         bg="white"
                         )
rgo_heading.pack(padx=10, pady=10, anchor="w")

# Raw material tabs
# Create notebook widget
tab_control = ttk.Notebook(window)

# Create tabs using the make_tabs procedure from the news screen,
# new parameters are added specifically, so that it is tailored to tabs in this screen.
def make_tabs(tab_name, op_time, op_efficiency, op_total_output, image_link):
    tab = ttk.Frame(tab_control)
    # Add tab name
    tab_control.add(tab, text=tab_name)
    tab_control.pack(expand=1, fill="both")

    # Image
    open_image = Image.open(image_link)
    mat_photo = ImageTk.PhotoImage(open_image)
    mat_photo_lbl = tk.Label(window, image=mat_photo)
    mat_photo_lbl.pack(padx=10, side="right")

    # Additional labels and buttons for displaying information of the raw materials.
    start_op_btn = tk.Button(tab, text="Start", font=('Arial', 16))
    start_op_btn.pack(anchor="w", padx=10, pady=10)

    ttk.Label(tab, text="Time: " + op_time, font=('Arial', 16)).pack(padx=10, pady=10, anchor="w")
    ttk.Label(tab, text="Efficiency: " + op_efficiency, font=('Arial', 16)).pack(padx=10, pady=10, anchor="w")
    ttk.Label(tab, text="Total output: " + op_total_output, font=('Arial', 16)).pack(padx=10, pady=10, anchor="w")

    collect_btn = tk.Button(tab, text="Collect", font=('Arial', 16))
    collect_btn.pack()


window.mainloop()



