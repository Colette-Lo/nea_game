import json
import random
from profile_screen import tryscreen
from scenario_decision_screen import case_manager


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


# the list of historical events that the player has solved
done_real_case = case_manager.done_cases
# load the event
events_values = load_values('all_events.json')
levels = ["lic_events", "mic_events", "hic_events"]

# for scenario decision screen
# find the level a case belongs to
def find_case_level(event_dict, keys_value, lvl_list):
    for i in range(3):
    #     event_name = event_dict[levels[i]]["name"]
    #     if event_name == keys_value:
    #         case_level = i
    # return case_level
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
        current_level = tryscreen.get_level()

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


# Testing section

# Calls
print(done_real_case)
try_choose_next = choose_case(done_real_case, events_values, real_events_graph, levels)
print(try_choose_next)
# print(events_values)