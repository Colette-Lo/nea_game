import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from screens import Screen
from object_dictionaries import prod


# # Create window
# window = tk.Tk()
# window.geometry("1920x1080")
# window.title("Country Simulation")
#
# # Title
# rgo_heading =  tk.Label(window,
#                          text="Production",
#                          font=('Arial', 30),
#                          bg="white"
#                          )
# rgo_heading.pack(padx=10, pady=10, anchor="w")
#
# # Products tabs
# # Create notebook widget
# tab_control = ttk.Notebook(window)
#
#
# def make_tabs(tab_name, good_name, location, efficiency, firm_output, image_link):
#     tab = ttk.Frame(tab_control)
#     # Add tab name
#     tab_control.add(tab, text=tab_name)
#     tab_control.pack(expand=1, fill="both")
#
#     # Image
#     open_image = Image.open(image_link)
#     product_photo = ImageTk.PhotoImage(open_image)
#     product_photo_lbl = ttk.Label(window, image = product_photo)
#     product_photo_lbl.pack(padx=10, side="right")
#
#     # Labels for information of the firm
#
#     ttk.Label(tab, text="Product: " + good_name, font=('Arial', 16)).pack(padx=10, pady=10, anchor="w")
#     ttk.Label(tab, text="Location: " + location, font=('Arial', 16)).pack(padx=10, pady=10, anchor="w")
#     ttk.Label(tab, text="Efficiency: " + efficiency, font=('Arial', 16)).pack(padx=10, pady=10, anchor="w")
#     ttk.Label(tab, text="Output: " + firm_output, font=('Arial', 16)).pack(padx=10, pady=10, anchor="w")
#
#
# window.mainloop()

class ProductionScreen(Screen):
    def __init__(self):
        super().__init__()
        self.heading = tk.Label(self,
                         text="Production",
                         font=('Arial', 30),
                         bg="white"
                         )
        self.heading.pack(padx=10, pady=10, anchor="w")

        self.production_notebook = ttk.Notebook(self, width=900, height=600)
        self.production_notebook.pack(padx=10, pady=10)


class ProducitonTab(tk.Frame):
    def __init__(self, master_notebook, tab_name, good_name, location, efficiency, image_link):
        super().__init__()

        # add itself to the notebook
        master_notebook.add(self, text=tab_name)

        # Using attributes to store the parameters
        self.product = good_name
        self.location = location
        self.efficiency = efficiency
        self.firm_output = 0.0
        self.image_path = image_link
        self.product_img_opened = []

        self.unit_cost = 0.0
        self.nearby_resources = []
        self.tech_list = []

        # Displaying the image immediately
        self.show_material()

        tk.Label(self, text="Product: " + self.product, font=('Arial', 20)).pack(padx=10, pady=10, anchor="w")
        tk.Label(self, text="Location: " + self.location, font=('Arial', 20)).pack(padx=10, pady=10, anchor="w")
        tk.Label(self, text="Efficiency: " + str(self.efficiency), font=('Arial', 20)).pack(padx=10, pady=10,anchor="w")
        tk.Label(self, text="Output: " + str(self.firm_output), font=('Arial', 20)).pack(padx=10, pady=10, anchor="w")

    def show_material(self):
        open_product_img = Image.open(self.image_path)
        product_file = ImageTk.PhotoImage(open_product_img)

        self.product_img_opened.append(product_file)

        product_lbl = tk.Label(self, image=product_file)
        product_lbl.pack(anchor="e", padx=10, pady=10)

    def unit_cost_change(self):
        pass

    def adjust_efficiency(self):
        pass

    def marginal_cost(self, unit_cost, quantity):
        pass

    def profit_max_quantity(self, price):
        pm_quantity = 0

        while self.marginal_cost < price:
            pm_quantity += 1
        return pm_quantity

    def total_cost(self, good, unit_cost):
        pass

# main
prod_screen = ProductionScreen()

# # low income stage
# firm1 = ProducitonTab(prod_screen.production_notebook,
#                       prod[0]["firm_name"],
#                       prod[0]["product_name"],
#                       prod[0]["location"],
#                       prod[0]["firm_efficiency"],
#                       prod[0]["image_path"]
#                       )
# firm2 = ProducitonTab(prod_screen.production_notebook,
#                       prod[1]["firm_name"],
#                       prod[1]["product_name"],
#                       prod[1]["location"],
#                       prod[1]["firm_efficiency"],
#                       prod[1]["image_path"]
#                       )
# firm3 = ProducitonTab(prod_screen.production_notebook,
#                       prod[2]["firm_name"],
#                       prod[2]["product_name"],
#                       prod[2]["location"],
#                       prod[2]["firm_efficiency"],
#                       prod[2]["image_path"]
#                       )
# firm4 = ProducitonTab(prod_screen.production_notebook,
#                       prod[3]["firm_name"],
#                       prod[3]["product_name"],
#                       prod[3]["location"],
#                       prod[3]["firm_efficiency"],
#                       prod[3]["image_path"]
#                       )
# firm5 = ProducitonTab(prod_screen.production_notebook,
#                       prod[4]["firm_name"],
#                       prod[4]["product_name"],
#                       prod[4]["location"],
#                       prod[4]["firm_efficiency"],
#                       prod[4]["image_path"]
#                       )
# # middle income stage
# firm6 = ProducitonTab(prod_screen.production_notebook,
#                       prod[5]["firm_name"],
#                       prod[5]["product_name"],
#                       prod[5]["location"],
#                       prod[5]["firm_efficiency"],
#                       prod[5]["image_path"]
#                       )
# firm7 = ProducitonTab(prod_screen.production_notebook,
#                       prod[6]["firm_name"],
#                       prod[6]["product_name"],
#                       prod[6]["location"],
#                       prod[6]["firm_efficiency"],
#                       prod[6]["image_path"]
#                       )
# firm8 = ProducitonTab(prod_screen.production_notebook,
#                       prod[7]["firm_name"],
#                       prod[7]["product_name"],
#                       prod[7]["location"],
#                       prod[7]["firm_efficiency"],
#                       prod[7]["image_path"]
#                       )
# # high income stage
# firm9 = ProducitonTab(prod_screen.production_notebook,
#                       prod[8]["firm_name"],
#                       prod[8]["product_name"],
#                       prod[8]["location"],
#                       prod[8]["firm_efficiency"],
#                       prod[8]["image_path"]
#                       )
# firm10 = ProducitonTab(prod_screen.production_notebook,
#                        prod[9]["firm_name"],
#                        prod[9]["product_name"],
#                        prod[9]["location"],
#                        prod[9]["firm_efficiency"],
#                        prod[9]["image_path"]
#                        )

prod_screen.mainloop()