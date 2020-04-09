"""
Example triage system that lays out the necessary information to implement another system.
"""
from typing import List

params = {
    "heart_rate": None,
    "blood_pressure": None
}


# subscribe() returns a list of parameters the triage system uses
def subscribe() -> List[str]:
    return list(params.keys())


# update() gives you the person object that has relevant updated parameters
def update(person):
    params["heart_rate"] = person.get_data("heart_rate")
    params["blood_pressure"] = person.get_data("blood_pressure")
    print(person.params)
