import tkinter as tk

class ScreenManager():
    def __init__(self):
        self.current_screen = None
        self.all_screens = {}

    def add_new(self, screen_name, screen_object, *args, **kwargs):
        # record the screen object as ready to be created using load_screen
        self.all_screens[screen_name] = screen_object(*args, **kwargs)

    def load_screen(self, screen_name, *args, **kwargs):
        if screen_name in self.all_screens:
            # retrieve the screen object and display it
            self.current_screen = self.get_screen_obj(screen_name)
            self.current_screen.mainloop()
        else:
            print("Screen is not in manager.")

    def get_screen_obj(self, screen_name):
        if screen_name in self.all_screens:
            return self.all_screens[screen_name]

my_screen_manager = ScreenManager()
