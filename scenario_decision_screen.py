import tkinter as tk

# Scenario screen where the player choose a policy
# Create the window
window = tk.Tk()

# Provide the resolution and title of the window.
window.geometry("1200x650")
window.title("Scenario")

# Heading
page_heading = tk.Label(window,
                        text="Scenario",
                        font=('Arial', 20),
                        bg="white",
                        width=20,
                        height=1
                        )
page_heading.pack(padx=10, pady=30)

# The description of the problem.
description = tk.Label(window,
                       text="Description",
                       font=('Arial', 20),
                       bg="white",
                       height=7,
                       width=45)
description.pack(pady=10)

# Option descriptions
# Option 1
option1 = tk.Label(window,
                       text="Option 1",
                       font=('Arial', 16),
                       bg="white",
                       height=10,
                       width=22)
option1.pack(padx=10, side="left")

option_button1 = tk.Radiobutton(window,
                         text="Option 1",
                         font=('Arial', 14))
option_button1.pack(side="left")

# Option 2
option2 = tk.Label(window,
                       text="Option 2",
                       font=('Arial', 16),
                       bg="white",
                       height=10,
                       width=22)
option2.pack(padx=10, side="left")

option_button2 = tk.Radiobutton(window,
                         text="Option 2",
                         font=('Arial', 14))
option_button2.pack(side="left")

# Option 3
option3 = tk.Label(window,
                       text="Option 3",
                       font=('Arial', 16),
                       bg="white",
                       height=10,
                       width=22)
option3.pack(padx=10, side="left")

option_button3 = tk.Radiobutton(window,
                         text="Option 3",
                         font=('Arial', 14))
option_button3.pack(side="left")

window.mainloop()








