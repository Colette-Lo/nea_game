import tkinter as tk
from tkinter import Frame
import matplotlib.pyplot as plt
from screens import Screen
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
class BudgetCalculations():
    def __init__(self, start_tax, start_spending, start_debt):
        self.new_tax = start_tax
        self.new_spending = start_spending
        self.new_debt = start_debt

    def cal_tax(self, modifier):
        self.new_tax *= (1 + modifier)
        return self.new_tax

    def cal_spending(self, modifier):
        self.new_spending *= (1 + modifier)
        return self.new_spending

    def cal_debt(self, modifier):
        self.new_debt *= (1 + modifier)
        return self.new_debt

cal_budget = BudgetCalculations(100, 50, 0)

class BudgetScreen(Screen):
    def __init__(self):
        super().__init__()
        self.heading = tk.Label(self,
                                text="Budget",
                                font=('Arial', 30),
                                bg="white",
                                width=10,
                                height=2
                                )
        self.heading.pack(padx=20, anchor='w')

        self.tax_value = cal_budget.new_tax
        self.spending_value = cal_budget.new_spending
        self.debt_value = cal_budget.new_debt

        # use a frame to contain everything other than the pie chart
        self.labels_frame = tk.Frame(self, borderwidth=5)
        self.labels_frame.pack(padx=(0, 90), anchor="n", side = "right")
        # add spacing between rows to separate labels

        self.tax_section =  tk.Label(self.labels_frame,
                                text=("Tax:", self.tax_value),
                                font=('Arial', 20),
                                bg="white",
                                width=40,
                                height=4
                                )
        self.tax_section.grid(row=0, column=0, pady=10)

        self.spending_section =  tk.Label(self.labels_frame,
                                text=("Spending:", self.spending_value),
                                font=('Arial', 20),
                                bg="white",
                                width=40,
                                height=4
                                )
        self.spending_section.grid(row=1, column=0, pady=10)

        self.debt_section =  tk.Label(self.labels_frame,
                             text=("National debt:", self.debt_value),
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
        self.pie_chart_data = [self.tax_value, self.spending_value]

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
