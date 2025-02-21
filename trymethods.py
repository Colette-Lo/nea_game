# import all classes/methods
# from the tkinter module
import tkinter
from tkinter import messagebox

import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
# For pie chart in Budget
# plot function is created for
# plotting the graph in
# tkinter window
# def plot():
#     # the figure that will contain the plot
#     fig = Figure(figsize=(5, 5),
#                  dpi=80)
#
#     # values for the pie chart
#     tax_value = 30000
#     spending_value = 100000
#     pie_chart_data = np.array([tax_value, spending_value])
#     my_labels = ["Tax revenue", "Gov spending"]
#
#     # adding the subplot
#     ax = fig.add_subplot(111)
#
#     # plotting the graph
#     ax.pie(pie_chart_data, labels=my_labels, startangle=90, shadow=True)
#
#     # ax.show()
#     ## does not need show(). add to report how this mistake was fixed.
#
#     # creating the Tkinter canvas
#     # containing the Matplotlib figure
#     canvas = FigureCanvasTkAgg(fig,
#                                master=my_frame)
#
#     # placing the canvas on the Tkinter window
#     canvas.get_tk_widget().grid(row=0, column=0, columnspan=3)
#     # making sure the graph is up to date
#     canvas.draw()
#
#
# the main Tkinter window
window = Tk()

# setting the title
window.title('Plotting in Tkinter')

# dimensions of the main window
# window.geometry("1000x700")
#
# # make a label?
# plot_label = Label(master=window,
#                    text="Budget",
#                    font=("Helvetica", 20)
#                    )
# # place the button
# # in main window
# plot_label.pack(anchor="n", side="left")
#
# # frame that holds the plot
# my_frame = Frame(window)
# # positioning on the left of the screen
# my_frame.pack(anchor="w", side="left")
# plot()


# run the gui
window.mainloop()

# functions for indicators

gdp = 0.0
life_ex = 0.0
