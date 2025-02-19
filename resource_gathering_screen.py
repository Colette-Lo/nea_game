import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from screens import Screen
from tab_method import CreateNotebook

# # Create window
# window = tk.Tk()
# window.geometry("1920x1080")
# window.title("Country Simulation")
#
# # Title
# rgo_heading =  tk.Label(window,
#                          text="Resource gathering operations",
#                          font=('Arial', 30),
#                          bg="white"
#                          )
# rgo_heading.pack(padx=10, pady=10, anchor="w")
#
# # Raw material tabs
# # Create notebook widget
# tab_control = ttk.Notebook(window)
#
# # Create tabs using the make_tabs procedure from the news screen,
# # new parameters are added specifically, so that it is tailored to tabs in this screen.
# def make_tabs(tab_name, op_time, op_efficiency, op_total_output, image_link):
#     tab = ttk.Frame(tab_control)
#     # Add tab name
#     tab_control.add(tab, text=tab_name)
#     tab_control.pack(expand=1, fill="both")
#
#     # Image
#     open_image = Image.open(image_link)
#     mat_photo = ImageTk.PhotoImage(open_image)
#     mat_photo_lbl = ttk.Label(window, image=mat_photo)
#     mat_photo_lbl.pack(padx=10, side="right")
#
#     # Additional labels and buttons for displaying information of the raw materials.
#     start_op_btn = tk.Button(tab, text="Start", font=('Arial', 16))
#     start_op_btn.pack(anchor="w", padx=10, pady=10)
#
#     ttk.Label(tab, text="Time: " + op_time, font=('Arial', 16)).pack(padx=10, pady=10, anchor="w")
#     ttk.Label(tab, text="Efficiency: " + op_efficiency, font=('Arial', 16)).pack(padx=10, pady=10, anchor="w")
#     ttk.Label(tab, text="Total output: " + op_total_output, font=('Arial', 16)).pack(padx=10, pady=10, anchor="w")
#
#     collect_btn = tk.Button(tab, text="Collect", font=('Arial', 16))
#     collect_btn.pack()
#
#
# window.mainloop()

class ResourceGatheringScreen(Screen):
    def __init__(self, material_img, op_time, op_efficiency, op_total_output):
        super().__init__()
        self.heading = tk.Label(self,
                                text="Resource Gathering Operations",
                                font=('Arial', 30),
                                bg="white",
                                width=10,
                                height=2
                                )
        self.heading.pack(padx=20, anchor='w')

        # new notebook
        self.rgo_notebook = ttk.Notebook(self)
        self.rgo_notebook.pack(padx=10, pady=10)

        # list of dictionaries of raw materials
        # name, image, time, efficiency, output
        self.materials = [{"name": "",
                           "image": "",
                           "time": "", "efficiency": "", "output": "" }
                          ]

        # image of the material
        self.material_image_path = material_img
        self.material_img_opened = []

        # display the image immediately
        self.show_material()

        # button for starting gathering
        self.start_op_btn = tk.Button(self, text="Start", font=('Arial', 16), command=self.click_start)
        self.start_op_btn.pack(anchor="w", padx=10, pady=10)

        # button for collecting resources gathered
        self.collect_btn = tk.Button(self, text="Collect", font=('Arial', 16), command=self.click_collect)
        self.collect_btn.pack()

        # labels displaying the operation time, efficiency, total output
        self.time_label = ttk.Label(self, text="Time: " + op_time, font=('Arial', 16))
        self.time_label.pack(padx=10, pady=10, anchor="w")

        self.efficiency_label = ttk.Label(self, text="Efficiency: " + op_efficiency, font=('Arial', 16))
        self.efficiency_label.pack(padx=10, pady=10, anchor="w")

        self.output_label = ttk.Label(self, text="Total output: " + op_total_output, font=('Arial', 16))
        self.output_label.pack(padx=10, pady=10, anchor="w")


    def show_material(self):
        open_mat_img = Image.open(self.material_image_path)
        mat_file = ImageTk.PhotoImage(open_mat_img)

        self.material_img_opened.append(mat_file)

        mat_lbl = tk.Label(self.rgo_notebook, image=mat_file)
        mat_lbl.pack()

    def operation_tab(self):
        pass

    def click_start(self):
        pass

    def click_collect(self):
        pass
