import tkinter as tk
from tkinter import ttk
from screens import Screen
from game_objects import *

class TradeScreen(Screen):
    def __init__(self, product_list, price_list, sold_list):
        super().__init__()
        self.heading =  tk.Label(self,
                                 text="Trade",
                                 font=('Arial', 30),
                                 bg="white",
                                 width=10
                                 )
        self.heading.pack(padx=10, pady=10, anchor="w")

        self.products = product_list
        self.prices = price_list
        self.sold = sold_list

        self.table = ttk.Treeview(self, columns=('Product', 'Price', 'Sold'), show='headings')
        self.table.heading('Product', text='Product')
        self.table.heading('Price', text='Price')
        self.table.heading('Sold', text='Sold')

        self.table.pack(anchor='e', padx=100, expand=True, fill='both')

        for i in range(len(self.products) - 1):
            product = self.products[i].name
            price = self.prices[i]
            sold = self.sold[i]
            self.table.insert(parent = '',
                              index = 0,
                              values = (product, price, sold)
                              )