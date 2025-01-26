import tkinter as tk
from screens import Screen

# # Where the context of the historical event is displayed.
# # Create the window
# window = tk.Tk()
#
# # Provide the resolution and title of the window.
# window.geometry("700x500")
# window.title("Information Box")
#
# # Heading
# page_heading = tk.Label(window,
#                         text="Context",
#                         font=('Arial', 20),
#                         bg="white",
#                         width=20,
#                         height=1
#                         )
# page_heading.pack(padx=10, pady=30)
#
# # Content
# description = tk.Label(window,
#                        text="Description",
#                        font=('Arial', 20),
#                        bg="white",
#                        height=10,
#                        width=35)
# description.pack(pady=10)
#
#
# window.mainloop()
#


## WAITTTTT
## parameter method COULD work
## If what we do is:
## for each scenario, case, whatever we feed different values to the screen
## so that for each case the screen would acc be unique and specific.
## and dont have to worry about the other cases until they are referenced
## with this being said all the other possible cases and their values do not acc matter
## until its their turn to show up.

class ScenerioInfoScreen(Screen):
    def __init__(self, context_info):
        super().__init__()
        self.title("Information Box")
        self.geometry("700x500")
        self.heading = tk.Label(self,
                                text="Context",
                                font=('Arial', 20),
                                bg="white",
                                width=20,
                                height=1
                                )
        self.heading.pack(padx=10, pady=30)

        self.description = tk.Label(self,
                                    text=context_info,
                                    font=('Arial', 20),
                                    bg="white",
                                    width=20
                                    )
