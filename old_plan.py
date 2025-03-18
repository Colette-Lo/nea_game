import random
import json

# reading data from a json file
def load_values(file):
    with open(file, 'r') as open_json:
        my_values = json.load(open_json)
    return my_values

# load the event
events_values = load_values('my_events.json')

# fake plan

# select an event that has not been solved randomly
def choose_random_event(event_list, solved):
    # Extract the list of events
    all_events_data = event_list["events"]
    # List of unsolved events
    available_events = []

    # Add unsolved events to the available list
    for event in all_events_data:
        if event["name"] not in solved:
            available_events.append(event)
    # If no unsolved, return nothing
    if not available_events:
        print("No more events available.")
        return None

    chosen = random.choice(available_events)
    solved.append(chosen["name"])
    return chosen


# simulate event selection
def test_event_generation():
    event_data = events_values # Load event data
    solved_events = []  # Track completed events

    for i in range(5):  # Simulate assigning 5 events
        next_event = choose_random_event(event_data, solved_events)

        if next_event is None:
            print("No more events available for testing.")
            break

        print("Generated Event:", next_event["name"])

test_event_generation()