# Using the library tkinter to create user interfaces.
import tkinter as tk

# Start screen
# Create the window for the start screen.
window = tk.Tk()

# Provide the resolution and title of the window.
window.geometry("1920x1080")
window.title("Country Simulation")

# Show the name of the game on the start screen
game_title = tk.Label(window,
                      text="Country Simulation",
                      font=('Arial', 40),
                      width=20,
                      height=2,
                      bg="white"
                      )
game_title.pack(padx=10, pady=200)

# Create the start button. The user clicks it if they want to start playing.
start_button = tk.Button(window,
                         text="Start",
                         font=('Arial', 30),
                         width=10,
                         bg="white",
                         fg="red"
                         )
start_button.pack()

window.mainloop()







# For action:
# If this is the first time playing the game, go to initial set up.
# If not, go straight to the home page.
