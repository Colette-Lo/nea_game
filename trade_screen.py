import tkinter as tk
from tkinter import ttk

from matplotlib.font_manager import fontManager

# Create window
window = tk.Tk()
window.geometry("1920x1080")
window.title("Country Simulation")

# Title
trade_table_heading =  tk.Label(window,
                         text="Trade",
                         font=('Arial', 30),
                         bg="white",
                         width=10
                         )
trade_table_heading.pack(padx=10, pady=10, anchor="w")

# Production button
production_button = tk.Button(window,
                         text="Production",
                         font=('Arial', 30),
                         width=10,
                         bg="white"
                         )
production_button.pack(anchor='w')


# Trade table
products_list = []
price_list = []
sold_list = []

# data will show when calculations are implemented later.

# Create the table, name the columns
table = ttk.Treeview(window, columns=('Product', 'Price', 'Sold'), show='headings')

# Add headings to the table
table.heading('Product', text='Product')
table.heading('Price', text='Price')
table.heading('Sold', text='Sold')

table.pack(anchor='e', padx=100, expand=True, fill='both')

# Insert values into the table
for i in range(len(products_list)-1):
    product = products_list[i]
    price = price_list[i]
    sold = sold_list[i]
    table.insert(parent = '', index = 0, values = (product, price, sold))

window.mainloop()



