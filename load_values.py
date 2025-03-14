import json

def load_events(file):
    with open(file, 'r') as event_json:
        event_values = json.load(event_json)
    return event_values