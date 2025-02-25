import tkinter as tk
from tkinter import ttk

from screens import Screen

project_tree = {
    "Agricultural Machinery":["Semi-Automated Manufacturing Plants"],
    "Rural Road & Bridge Expansion":["Smart Grid & Public Transit Upgrade"],
    "Affordable Biofuel Production":["Solar & Wind Energy"],
    "Semi-Automated Manufacturing Plants":["Robotics & AI-Driven Factories"],
    "Smart Grid & Public Transit Upgrade":["Smart Cities"],
    "Solar & Wind Energy":["Carbon Capture & Sustainable Synthetic Fuels"],
    "Robotics & AI-Driven Factories": None,
    "Smart Cities": None,
    "Carbon Capture & Sustainable Synthetic Fuels": None
}

class TechnologyScreen(Screen):
    def __init__(self):
        super().__init__()

        self.heading = tk.Label(self,
                                text="Production",
                                font=('Arial', 30),
                                bg="white"
                                )
        self.heading.pack(padx=10, pady=10, anchor="w")

        # dividing the screen into three sections
        self.tech_screen_frame = tk.Frame(self, borderwidth=0)
        self.tech_screen_frame.columnconfigure(0, weight=1)
        self.tech_screen_frame.pack(padx=10, pady=10, anchor='n')

        # Mechanisation
        self.mech_lbl =  tk.Label(self.tech_screen_frame,
                             text="Mechanisation",
                             font=('Arial', 20),
                             bg="white",
                             width=25,
                             height=2
                            )
        self.mech_lbl.grid(row=0, column=0, padx=40, pady=10, sticky='ew')
        self.mech_notebook = ttk.Notebook(self.tech_screen_frame)
        self.mech_notebook.grid(row=1, column=0, sticky='nsew')

        # Infrastructure
        self.infra_lbl =  tk.Label(self.tech_screen_frame,
                                text="Infrastructure",
                                font=('Arial', 20),
                                bg="white",
                                width=25,
                                height=2
                                )
        self.infra_lbl.grid(row=0, column=1, padx=40, pady=10, sticky='ew')
        self.infra_notebook = ttk.Notebook(self.tech_screen_frame)
        self.infra_notebook.grid(row=1, column=1, sticky='nsew')

        # Chemistry and power
        self.chem_power_lbl =  tk.Label(self.tech_screen_frame,
                                text="Chemistry and power",
                                font=('Arial', 20),
                                bg="white",
                                width=25,
                                height=2
                                )
        self.chem_power_lbl.grid(row=0, column=2, padx=40, pady=10, sticky='ew')
        self.chem_notebook = ttk.Notebook(self.tech_screen_frame)
        self.chem_notebook.grid(row=1, column=2, sticky='nsew')


class ProjectTab(tk.Frame):
    def __init__(self, master_notebook, proj_name, content, time_required, invested, children):
        super().__init__()

        # add itself to the notebook
        master_notebook.add(self, text=proj_name)

        # attributes
        self.content = tk.Label(self, text=content, font=('Arial', 20))
        self.content.pack(padx=10, pady=10, anchor="w")

        self.research_time = time_required
        self.invested = invested
        self.children_proj = children


        # Research button
        self.research_btn = tk.Button(self, text=("Research"), font=('Arial', 14))
        self.research_btn.pack(padx=10, pady=10, anchor='s')


# main
tech_screen = TechnologyScreen()

p1 = ProjectTab(tech_screen.mech_notebook, "Agricultural Machinery", "this is the first project")
p2 = ProjectTab(tech_screen.infra_notebook, "Tunnel", "this is the second project")
p3 = ProjectTab(tech_screen.chem_notebook, "Electricity", "this is the third project")

tech_screen.mainloop()