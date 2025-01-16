import tkinter as tk
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

# A procedure to make a tab.
def make_tabs(tab_name, text_title):
    tab = ttk.Frame(tab_control)
    # Add tab name
    tab_control.add(tab, text=tab_name)
    tab_control.pack(expand=1, fill="both")

    # Add tab title
    ttk.Label(tab, text=text_title).grid(column=0,
                                       row=0,
                                       padx=30,
                                       pady=30
                                       )

# Make two tabs
tab1 = "News 1"
news_title1 = ""
make_tabs(tab1, news_title1)

tab2 = "News 2"
news_title2 = ""
make_tabs(tab2, news_title2)

window.mainloop()


