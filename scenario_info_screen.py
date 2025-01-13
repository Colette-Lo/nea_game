import tkinter as tk

# Where the context of the historical event is displayed.
# Create the window
window = tk.Tk()

# Provide the resolution and title of the window.
window.geometry("700x500")
window.title("Information Box")

# Heading
page_heading = tk.Label(window,
                        text="Context",
                        font=('Arial', 20),
                        bg="white",
                        width=20,
                        height=1
                        )
page_heading.pack(padx=10, pady=30)

# Content
description = tk.Label(window,
                       text="Description",
                       font=('Arial', 20),
                       bg="white",
                       height=10,
                       width=35)
description.pack(pady=10)


window.mainloop()





