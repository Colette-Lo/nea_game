import tkinter as tk
from tkinter import ttk
import time
from tkinter import messagebox

from game_state import my_screen_manager
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
    def __init__(self, master_notebook, proj_name, content, time_required, base_modifier, invested, initial_status):
        super().__init__(master_notebook)

        # add itself to the notebook
        master_notebook.add(self, text=proj_name)

        # attributes
        self.notebook = master_notebook
        self.proj_name = proj_name
        self.content = tk.Label(self, text=content, font=('Arial', 20))
        self.content.pack(padx=10, pady=10, anchor="w")
        self.start_time = 0
        self.research_time = time_required
        self.base_modifier = base_modifier
        self.invested = invested
        self.completed = False
        self.is_unlocked = initial_status
        self.child_proj = None
        # self.has_parent = False



        # Research button
        self.research_btn = tk.Button(self, text=("Research"), font=('Arial', 14), command = self.research)
        self.research_btn.pack(padx=10, pady=10, anchor='s')

    def set_child(self, child):
        self.child_proj = child
        # child project is initially set to not visible
        if self.child_proj is not None:
            self.notebook.forget(self.child_proj)

    def unlock_child(self):
        self.child_proj.is_unlocked = True
        # Re-add the child tab
        self.notebook.add(self.child_proj.tab, text=self.child_proj.proj_name)
        print("Child project unlocked!")

    def research(self):
        if self.is_unlocked:
            self.start_time = time.time()
            self.completed = False
            messagebox.showinfo("Status", "Research started")
            print("Research started")
        else:
            messagebox.showwarning("Warning", "Project is locked.")
            print("Project is locked")
        pass

    def is_completed(self):
        if self.start_time is None:
            return False
        time_passed = time.time() - self.start_time
        if time_passed > self.research_time:
            self.completed = True

            if self.child_proj is not None:
                self.unlock_child()
            messagebox.showinfo("Status", "Research completed")
            print("Research completed")
        return self.completed

    def get_effect(self):
        if self.completed:
            return self.base_modifier
        else:
            return 0


# main

my_screen_manager.add_new("my_tech", TechnologyScreen)
tech_screen_obj = my_screen_manager.get_screen_obj("my_tech")
# 1st level
mech_lvl1 = ProjectTab(tech_screen_obj.mech_notebook, "Agricultural Machinery", "this is the first project", 40, 0.1, 0,  True)
infra_lvl1 = ProjectTab(tech_screen_obj.infra_notebook, "Rural Road & Bridge Expansion", "this is the second project", 40, 0.1,0,  True)
chem_lvl = ProjectTab(tech_screen_obj.chem_notebook, "Affordable Biofuel Production", "this is the third project", 40, 0.1,0,  True)

# 2nd level
mech_lvl2 = ProjectTab(tech_screen_obj.mech_notebook, "Semi-Automated Manufacturing Plants", "this is the 4th project", 40, 0.1,0,  False)
infra_lvl2 = ProjectTab(tech_screen_obj.infra_notebook, "Smart Grid & Public Transit Upgrade", "this is the 5th project", 40, 0.1,0,  False)
chem_lvl2 = ProjectTab(tech_screen_obj.chem_notebook, "Solar & Wind Energy", "this is the 6th project", 40, 0.1,0,  False)

# 3rd level
mech_lvl3 = ProjectTab(tech_screen_obj.mech_notebook, "Robotics & AI-Driven Factories", "this is the 7th project", 40, 0.1,0, False)
infra_lvl3 = ProjectTab(tech_screen_obj.infra_notebook, "Smart Cities", "this is the 8th project", 40, 0.1,0, False)
chem_lvl3 = ProjectTab(tech_screen_obj.chem_notebook, "Carbon Capture & Sustainable Synthetic Fuels", "this is the 9th project", 40, 0.1,0, False)
#project_list = [mech_lvl1, infra_lvl1, chem_lvl, mech_lvl2, infra_lvl2, chem_lvl2]

mech_lvl1.set_child(mech_lvl2)
mech_lvl2.set_child(mech_lvl3)
infra_lvl1.set_child(infra_lvl2)
infra_lvl2.set_child(infra_lvl3)
chem_lvl.set_child(chem_lvl2)
chem_lvl2.set_child(chem_lvl3)