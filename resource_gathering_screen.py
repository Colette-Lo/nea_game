import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
from screens import Screen
import time
from object_dictionaries import materials
from game_objects import *
from trymethods import RGOManager

op_manager = RGOManager()

class ResourceGatheringScreen(Screen):
    def __init__(self):
        super().__init__()
        self.heading = tk.Label(self,
                                text="Resource Gathering Operations",
                                font=('Arial', 30),
                                bg="white",
                                height=2
                                )
        self.heading.pack(padx=20, anchor='w')

        # new notebook
        self.rgo_notebook = ttk.Notebook(self, width=900, height=600)
        self.rgo_notebook.pack(padx=10, pady=10)


class ResourceTab(tk.Frame):
    def __init__(self, master_notebook, mat_name, material_img, op_time, op_efficiency, extract_cost):
        super().__init__()

        # add itself to the notebook
        master_notebook.add(self, text=mat_name)

        # storing the parameters
        self.resource_name = mat_name
        self.total_time = int(op_time)
        self.efficiency = float(op_efficiency)
        self.cost = extract_cost
        self.total_output = 0.0
        self.period_output = 1.0 # cannot start with 0
        self.finished = True
        self.start_time = 0

        # image of the material
        self.material_image_path = material_img
        self.material_img_opened = []

        # display the image immediately
        self.show_material()

        # button for starting gathering
        self.start_op_btn = tk.Button(self, text="Start", font=('Arial', 16), command=self.click_start)
        self.start_op_btn.pack(anchor="w", padx=10, pady=10)

        # labels displaying the operation time, efficiency, total output
        self.time_label = ttk.Label(self, text="Time(minutes): " + str(self.total_time/60), font=('Arial', 16))
        self.time_label.pack(padx=10, pady=20, anchor="w")

        self.efficiency_label = ttk.Label(self, text="Efficiency: " + op_efficiency, font=('Arial', 16))
        self.efficiency_label.pack(padx=10, pady=20, anchor="w")

        self.output_label = ttk.Label(self, text="Total output: " + str(self.total_output), font=('Arial', 16))
        self.output_label.pack(padx=10, pady=20, anchor="w")

        self.cost_label = ttk.Label(self, text="Cost: " + str(self.cost), font=('Arial', 16))
        self.cost_label.pack(padx=10, pady=20, anchor="w")

        # button for collecting resources gathered
        self.collect_btn = tk.Button(self, text="Collect", font=('Arial', 16), command = self.click_collect)
        self.collect_btn.pack(side="bottom", anchor="w", padx=10)

        # status of the operation
        self.is_active = False


    def show_material(self):
        open_mat_img = Image.open(self.material_image_path)
        mat_file = ImageTk.PhotoImage(open_mat_img)

        self.material_img_opened.append(mat_file)

        mat_lbl = tk.Label(self, image=mat_file)
        mat_lbl.pack(anchor="e", padx=10, pady=10)

    def click_start(self):
        if not op_manager.operations[self.resource_name]["status"]:
            # start gathering in the manager class
            op_manager.start_gathering(self.resource_name)
            # letting the player know
            messagebox.showinfo("Operation started", ("Collect after:"+ str(self.total_time//60)+ "minutes"))
        else:
            # letting the player know that the operation has already been started
            messagebox.showwarning("Warning", "Resource Gathering Operation is already active")

    # Scheduling progress updates every second
        self.after(1000, op_manager.get_current_progress(self.resource_name), self.resource_name)


    def click_collect(self):
        if op_manager.operations[self.resource_name]["collectable"]:
            # add gathered to total material has ever been collected
            op_manager.collect(self.resource_name)
            messagebox.showinfo("Operation completed", ("You have collected:"+ self.resource_name))
        else:
            messagebox.showwarning("Warning", "Cannot collect the resource yet")

# main
rgo_screen = ResourceGatheringScreen()
coal_tab = ResourceTab(rgo_screen.rgo_notebook,
                       materials[0]["name"],
                       materials[0]["image_path"],
                       materials[0]["operation_time"],
                       materials[0]["operation_efficiency"],
                       coal.ex_cost
                       )
oil_tab = ResourceTab(rgo_screen.rgo_notebook,
                       materials[1]["name"],
                       materials[1]["image_path"],
                       materials[1]["operation_time"],
                       materials[1]["operation_efficiency"],
                      oil.ex_cost
                       )
crops_tab = ResourceTab(rgo_screen.rgo_notebook,
                        materials[2]["name"],
                        materials[2]["image_path"],
                        materials[2]["operation_time"],
                        materials[2]["operation_efficiency"],
                        crops.ex_cost
                        )
metals_tab = ResourceTab(rgo_screen.rgo_notebook,
                         materials[3]["name"],
                         materials[3]["image_path"],
                         materials[3]["operation_time"],
                         materials[3]["operation_efficiency"],
                         metals.ex_cost
                         )
timber_tab = ResourceTab(rgo_screen.rgo_notebook,
                         materials[4]["name"],
                         materials[4]["image_path"],
                         materials[4]["operation_time"],
                         materials[4]["operation_efficiency"],
                         timber.ex_cost
                         )
wool_tab = ResourceTab(rgo_screen.rgo_notebook,
                       materials[5]["name"],
                       materials[5]["image_path"],
                       materials[5]["operation_time"],
                       materials[5]["operation_efficiency"],
                       wool.ex_cost
                       )

rgo_screen.mainloop()