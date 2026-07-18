"""
Its My Json Practice
"""

import json

def save_notes(note):
    with open ("data.json", "w") as f:
        json.dump (note, f)


def load_notes():
    try:
        with open ("data.json","r") as f:
            data = json.load(f)
            print(data)
    except FileNotFoundError:
        return {}




save_notes("name : Areeb")
load_notes()
