import tkinter as tk
from idlelib.configdialog import font_sample_text
from tkinter import ttk

# News screen to show the effect of the policy chosen.
# Create the window
window = tk.Tk()

# Provide the resolution and title of the window.
window.geometry("700x500")
window.title("News")

# Heading
page_heading = tk.Label(window,
                        text="News",
                        font=('Arial', 20),
                        bg="white",
                        width=20,
                        height=1
                        )
page_heading.pack(padx=10, pady=20)

# Create a notebook widget
tab_control = ttk.Notebook(window)

# Create two tabs
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

# Add tabs to notebook
tab_control.add(tab1,
                text="News 1")
tab_control.add(tab2,
                text="News 2")

tab_control.pack(expand=1, fill="both")

# News tab titles
ttk.Label(tab1, text="Title").grid(column=0,
                                   row=0,
                                   padx=30,
                                   pady=30
                                   )
ttk.Label(tab2, text="Title").grid(column=0,
                                   row=0,
                                   padx=30,
                                   pady=30)

window.mainloop()


