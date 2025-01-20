import tkinter as tk
from tkinter import ttk
from PIL.ImageOps import expand
from matplotlib.font_manager import fontManager
from numpy.ma.extras import row_stack, column_stack
from setuptools.logging import configure

# The screen where spending and income is displayed.
# Create window
window = tk.Tk()

# Provide the resolution and title of the window.
window.geometry("1920x1080")
window.title("Country Simulation")

# Show the heading
page_heading = tk.Label(window,
                        text="Technology",
                        font=('Arial', 30),
                        bg="white",
                        width=10,
                        height=2
                        )
page_heading.pack(padx=10, anchor='w')

# Sectors labels
# Label frame
# Procedure for organising labels side by side.
frame_name = tk.LabelFrame(window, borderwidth=0)
frame_name.columnconfigure(0, weight=1)
frame_name.pack(padx=10, pady=10, anchor='n')


# Mechanisation
mech_lbl =  tk.Label(frame_name,
                     text="Mechanisation",
                     font=('Arial', 20),
                     bg="white",
                     width=25,
                     height=2
                    )
mech_lbl.grid(row=0, column=0, padx=40, pady=10, sticky='ew')

# Infrastructure
infra_lbl =  tk.Label(frame_name,
                        text="Infrastructure",
                        font=('Arial', 20),
                        bg="white",
                        width=25,
                        height=2
                        )
infra_lbl.grid(row=0, column=1, padx=40, pady=10, sticky='ew')

# Chemistry and power
chem_power_lbl =  tk.Label(frame_name,
                        text="Chemistry and power",
                        font=('Arial', 20),
                        bg="white",
                        width=25,
                        height=2
                        )
chem_power_lbl.grid(row=0, column=2, padx=40, pady=10, sticky='ew')

# Project tabs
# Create one notebook widget for each sector
mech_tab_control = ttk.Notebook(window,
                                width=400,
                                height=900,
                                side=tk.LEFT
                                )

def make_tabs(tab_control, tab_name, content):
    tab = ttk.Frame(tab_control)
    # Add tab name
    tab_control.add(tab, text=tab_name)
    tab_control.pack()

    # Content
    ttk.Label(tab, text=content, font=('Arial', 14)).pack(padx=10, pady=10, anchor='w')

    # Research button
    research_btn = tk.Button(tab, text=("Research"), font=('Arial', 14))
    research_btn.pack(padx=10, pady=10, anchor='s')

stuff = 'edfg'
make_tabs(mech_tab_control, "project1", stuff)
window.mainloop()



