import json
import random
import time
from object_dictionaries import *
from game_state import my_screen_manager


# reading data from a json file
def load_values(file):
    with open(file, 'r') as open_json:
        my_values = json.load(open_json)
    return my_values

# Test data
# Scenario graph :)
real_events_graph = {"The Great Famine of Ireland (1845-1852)": ["The Debt Crisis of the 1980s", "The Asian Financial Crisis (1997)"],
                     "The Debt Crisis of the 1980s": ["The Bangladesh Garment Factory Collapse (2013)", "The Argentine Economic Crisis (1998-2002)"],
                     "The Bangladesh Garment Factory Collapse (2013)": ["The Greek Debt Crisis (2009)"],
                     "The Asian Financial Crisis (1997)":["The Argentine Economic Crisis (1998-2002)", "The Global Financial Crisis (2007-2008)"],
                     "The Argentine Economic Crisis (1998-2002)": ["The Greek Debt Crisis (2009)", "The 1973 Oil Crisis"],
                     "The Greek Debt Crisis (2009)": ["The Great Depression (1929)"],
                     "The Great Depression (1929)": ["The Global Financial Crisis (2007-2008)"],
                     "The Global Financial Crisis (2007-2008)": ["The 1973 Oil Crisis"],
                     "The 1973 Oil Crisis": []
}


class DecisionManager():
    def __init__(self):
        self.done_cases = []


# the list of historical events that the player has solved
case_manager = DecisionManager()
done_real_case = case_manager.done_cases
# load the event
events_values = load_values('all_events.json')
levels = ["lic_events", "mic_events", "hic_events"]

# for scenario decision screen
# find the level a case belongs to
def find_case_level(event_dict, keys_value, lvl_list):
    for i in range(3):
        for event in event_dict[lvl_list[i]]:
            if event["name"] == keys_value:
                return i


# find the event in the target level
def find_next_level_event(case_graph, event_data, latest_case, target_lvl):
    found = False
    while not found:
        for child_case in case_graph[latest_case]:
            child_case_lvl = find_case_level(event_data, child_case, levels)
            if child_case_lvl == target_lvl:
                found = True
    return child_case

# Determine what scenario to give the player
def choose_case(solved, event_list, case_graph, levels_list):
    profile_object = my_screen_manager.get_screen_obj("my_profile")
    # is this the first case
    if len(solved) == 0:
        # randomly choosing from 3 real cases
        case_index = random.randint(0, 2)
        next_event = event_list["lic_events"][case_index]
        solved.append(next_event["name"])
    else:
        # find the level the last case belongs to
        last_event_name = solved[-1]
        last_case_level = find_case_level(event_list, last_event_name, levels_list)
        # current level
        print(profile_object.level)
        current_level = profile_object.level

        # selecting the next event
        if last_case_level == current_level:
            next_event_name = case_graph[last_event_name][0]
        else:
            next_event_name = find_next_level_event(case_graph, event_list, last_event_name, current_level)
        # store the full dictionary
        for level in levels_list:
            for event in event_list[level]:
                if event["name"] == next_event_name:
                    next_event = event
    return next_event


class RGOManager():
    def __init__(self):

        # dictionary of all the operation
        # resource: {start_time, total_time, period_time, status, gathered, period_output, total_mat}
        self.operations = {
            "Coal": {"status": False, "collectable": False, "start_time": 0.0, "total_time": materials["Coal"]["operation_time"], "period_time": 0.0, "period_output": 0.0, "period_count": 0, "current_gathered": 0.0, "total_mat": 0.0},
            "Oil": {"status": False, "collectable": False, "start_time": 0.0, "total_time": materials["Oil"]["operation_time"], "period_time": 0.0, "period_output": 0.0, "period_count": 0, "current_gathered": 0.0, "total_mat": 0.0},
            "Crops": {"status": False, "collectable": False, "start_time": 0.0, "total_time": materials["Crops"]["operation_time"], "period_time": 0.0, "period_output": 0.0, "period_count": 0, "current_gathered": 0.0, "total_mat": 0.0},
            "Metals": {"status": False, "collectable": False, "start_time": 0.0, "total_time": materials["Metals"]["operation_time"], "period_time": 0.0, "period_output": 0.0, "period_count": 0, "current_gathered": 0.0, "total_mat": 0.0},
            "Timber": {"status": False, "collectable": False, "start_time": 0.0, "total_time": materials["Timber"]["operation_time"], "period_time": 0.0, "period_output": 0.0, "period_count": 0, "current_gathered": 0.0, "total_mat": 0.0},
            "Wool": {"status": False, "collectable": False, "start_time": 0.0, "total_time": materials["Wool"]["operation_time"], "period_time": 0.0, "period_output": 0.0, "period_count": 0, "current_gathered": 0.0, "total_mat": 0.0}
        }

    # checking if operation is active
    def is_active(self, resource_name):
        return self.operations[resource_name]["status"]

    # recording the start time
    def record_start(self, resource_name):
        self.operations[resource_name]["start_time"] = self.get_current()

    # get current time
    def get_current(self):
        return time.time()

    # adjusting the time requirements before starting a new operation
    def get_op_time(self, resource_name,  efficiency):
        self.operations[resource_name]["total_time"] *= (1 - efficiency)
        self.operations[resource_name]["period_time"] = round(self.operations[resource_name]["total_time"] / 5)

    # adjusting the period output before starting a new operation
    def get_period_output(self, resource_name, efficiency):
        self.operations[resource_name]["period_output"] = round(self.operations[resource_name]["period_output"] * (1+efficiency), 1)

    #####################################

    # when the start button is clicked
    def start_gathering(self, resource_name):
        self.operations[resource_name]["status"]  = True
        self.record_start(resource_name)
        self.get_op_time(resource_name, 1)


    # keep checking
    def get_current_progress(self, resource_name):
        if self.operations[resource_name]["period_count"] < 5:
            current_time = self.get_current()
            time_passed = current_time - self.operations[resource_name]["start_time"]
            # testing
            print(time_passed)
            print(self.operations[resource_name]["period_time"])
            if time_passed >= self.operations[resource_name]["period_time"]:
                self.operations[resource_name]["current_gathered"] += self.operations[resource_name]["period_output"]
                self.operations[resource_name]["period_count"] += 1
                # testing
                print(self.operations[resource_name]["period_count"])
        else:
            self.operations[resource_name]["collectable"] = True
            self.operations[resource_name]["period_count"] = 0
            self.operations[resource_name]["current_gathered"] = 0

    # when the collect button is clicked
    def collect(self, resource_name):
        if self.operations[resource_name]["collectable"]:
            self.operations[resource_name]["total_mat"] += self.operations[resource_name]["current_gathered"]
            print("You have collected", resource_name)
        else:
            print("Still gathering. Come back later!")
