from start_screen import StartScreen
from game_state import my_screen_manager

new_start = StartScreen
my_screen_manager.add_new("new_start", new_start)
my_screen_manager.load_screen("new_start")
