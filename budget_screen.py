import tkinter as tk
from tkinter import Frame

import matplotlib.pyplot as plt
from screens import Screen
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

#
# # The screen where spending and income is displayed.
# # Create window
# window = tk.Tk()
#
# # Provide the resolution and title of the window.
# window.geometry("1920x1080")
# window.title("Country Simulation")
#
# # Show the heading
# page_heading = tk.Label(window,
#                         text="Budget",
#                         font=('Arial', 30),
#                         bg="white",
#                         width=10,
#                         height=2
#                         )
# page_heading.pack(padx=10, anchor='w')
#
# # Bar chart
# # Chart dimensions
# canvas_width = 600
# canvas_height = 300
# bar_width = 55
# bar_spacing = 20
# top_margin = 30
#
# # Create canvas
# #def draw_chart(canvas, data):
# canvas = tk.Canvas(window,
#                    width=canvas_width,
#                    height=canvas_height,
#                    bg="white"
#                    )
# canvas.pack(side='left', fill='y')
#
# # need data to create bars.
#
# # Tax section label
# tax_section =  tk.Label(window,
#                         text="Tax:",
#                         font=('Arial', 20),
#                         bg="white",
#                         width=50,
#                         height=6
#                         )
# tax_section.pack(padx=10, pady=10)
#
# # Spending section label
# spending_section =  tk.Label(window,
#                         text="Spending:",
#                         font=('Arial', 20),
#                         bg="white",
#                         width=50,
#                         height=6
#                         )
# spending_section.pack(padx=10, pady=10)
#
# # National debt label
# debt_lbl =  tk.Label(window,
#                         text="National debt:",
#                         font=('Arial', 20),
#                         bg="white",
#                         width=50,
#                         height=2
#                         )
# debt_lbl.pack(padx=10, pady=10)
#
# # Education section label
# education_lbl =  tk.Label(window,
#                         text="Education spending (million):",
#                         font=('Arial', 20),
#                         bg="white",
#                         width=50,
#                         height=2
#                         )
# education_lbl.pack(padx=10, pady=10)
#
#
# # Education spending input stepper
# edu_spin = tk.Spinbox(window,
#                       from_=0,
#                       to=100,
#                       font=('Arial', 20),
#                       width=10
#                       )
# edu_spin.pack(padx=10, pady=10, anchor='s')
#
# window.mainloop()
#

class BudgetScreen(Screen):
    def __init__(self, tax_rev, spending_value, debt_value):
        super().__init__()
        self.heading = tk.Label(self,
                                text="Budget",
                                font=('Arial', 30),
                                bg="white",
                                width=10,
                                height=2
                                )
        self.heading.pack(padx=20, anchor='w')


        # use a frame to contain everything other than the pie chart
        self.labels_frame = tk.Frame(self, borderwidth=5)
        self.labels_frame.pack(padx=(0, 90), anchor="n", side = "right")
        # add spacing between rows to separate labels

        self.tax_section =  tk.Label(self.labels_frame,
                                text=("Tax:", tax_rev),
                                font=('Arial', 20),
                                bg="white",
                                width=40,
                                height=4
                                )
        self.tax_section.grid(row=0, column=0, pady=10)

        self.spending_section =  tk.Label(self.labels_frame,
                                text=("Spending:", spending_value),
                                font=('Arial', 20),
                                bg="white",
                                width=40,
                                height=4
                                )
        self.spending_section.grid(row=1, column=0, pady=10)

        self.debt_section =  tk.Label(self.labels_frame,
                             text=("National debt:", debt_value),
                             font=('Arial', 20),
                             bg="white",
                             width=40,
                             height=2
                             )
        self.debt_section.grid(row=2, column=0, pady=10)

        self.education_spent = 0.0
        self.education_section =  tk.Label(self.labels_frame,
                                text=("Education spending (million):", self.education_spent),
                                font=('Arial', 20),
                                bg="white",
                                width=40,
                                height=4
                                )
        self.education_section.grid(row=3, column=0, pady=10)

        self.education_stepper = tk.Spinbox(self.labels_frame,
                              from_=0,
                              to=100,
                              font=('Arial', 20),
                              width=20
                              )
        self.education_stepper.grid(row=4, column=0, pady=10)

        # organising the two pieces of data using a list
        # for plotting the graph
        self.pie_chart_data = [tax_rev, spending_value]

        # make a frame to hold the graph
        self.pie_frame = tk.Frame(self)
        self.pie_frame.pack(padx = (90, 0), anchor="w", side="left")

        # call the plotting method
        # so that the graph would always appear together with the screen
        self.make_pie_chart()

    def make_pie_chart(self):
        # the figure that will contain the pie chart
        fig = Figure(figsize=(7, 6),
                     dpi=80)

        # data and labels for the pie chart
        pie_chart_data = np.array(self.pie_chart_data)
        pie_labels = ["Tax revenue", "Gov spending"]

        # adding the subplot
        ax = fig.add_subplot(111)

        # plotting the pie chart
        ax.pie(pie_chart_data, labels=pie_labels, startangle=90, shadow=True)

        # creating the Tkinter canvas containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master=self.pie_frame)

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().grid(row=0, column=0, columnspan=3)

        # making sure the chart is up to date
        canvas.draw()

    def stepper_change(self):
        pass

trybudget = BudgetScreen(30000, 100000, 20000)
trybudget.mainloop()