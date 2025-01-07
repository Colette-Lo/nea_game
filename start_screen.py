# Using the library tkinter to create the user interfaces.
import tkinter as tk

# Start screen
# Create the window for the start screen.
window = tk.Tk()

# Provide the resolution and title of the window.
window.geometry("1920x1820")
window.title("Country Simulation")

# Show the name of the game on the start screen
game_title = tk.Label(window, text="Country Simulation", font=('Arial', 40))
game_title.pack(padx=10, pady=200)

# Create the start button. The user clicks it if they want to start playing.
start_button = tk.Button(window, text="Start", font=('Arial', 25))
start_button.pack()

window.mainloop()





