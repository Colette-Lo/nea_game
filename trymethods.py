import time
from object_dictionaries import *
import json

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
