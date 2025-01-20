import tkinter as tk

# The screen where spending and income is displayed.
# Create window
window = tk.Tk()

# Provide the resolution and title of the window.
window.geometry("1920x1080")
window.title("Country Simulation")

# Show the heading
page_heading = tk.Label(window,
                        text="Budget",
                        font=('Arial', 30),
                        bg="white",
                        width=10,
                        height=2
                        )
page_heading.pack(padx=10, anchor='w')

# Bar chart
# Chart dimensions
canvas_width = 600
canvas_height = 300
bar_width = 55
bar_spacing = 20
top_margin = 30

# Create canvas
#def draw_chart(canvas, data):
canvas = tk.Canvas(window,
                   width=canvas_width,
                   height=canvas_height,
                   bg="white"
                   )
canvas.pack(side='left', fill='y')

# need data to create bars.

# Tax section label
tax_section =  tk.Label(window,
                        text="Tax:",
                        font=('Arial', 20),
                        bg="white",
                        width=50,
                        height=6
                        )
tax_section.pack(padx=10, pady=10)

# Spending section label
spending_section =  tk.Label(window,
                        text="Spending:",
                        font=('Arial', 20),
                        bg="white",
                        width=50,
                        height=6
                        )
spending_section.pack(padx=10, pady=10)

# National debt label
debt_lbl =  tk.Label(window,
                        text="National debt:",
                        font=('Arial', 20),
                        bg="white",
                        width=50,
                        height=2
                        )
debt_lbl.pack(padx=10, pady=10)

# Education section label
education_lbl =  tk.Label(window,
                        text="Education spending (million):",
                        font=('Arial', 20),
                        bg="white",
                        width=50,
                        height=2
                        )
education_lbl.pack(padx=10, pady=10)


# Education spending input stepper
edu_spin = tk.Spinbox(window,
                      from_=0,
                      to=100,
                      font=('Arial', 20),
                      width=10
                      )
edu_spin.pack(padx=10, pady=10, anchor='s')

window.mainloop()


