"""
This file contains all functions needed to perform a START triage based on the findings at:
https://chemm.nlm.nih.gov/startadult.htm
"""

REQUIRED_PARAMS = {
    "can_walk": None,  # boolean value
    "breathing": None,  # boolean value
    "respiratory_rate": None,  # integer value
    "perfusion": None,  # (Radial pulse present), boolean value
    "capillary_refill": None,  # (In seconds) integer value
    "can_obey_commands": None  # boolean value
}


def subscribe():
    return list(REQUIRED_PARAMS.keys())


def update(person):
    temp = REQUIRED_PARAMS.copy()
    # TODO: Modify for loop to not change values if value did not change
    for param in temp:
        temp[param] = person.get_data(param)
    return get_severity(temp)


# Instead of returning a string return an int would save more space. We should have a general idea that
# a 3 refers to black tag, 2 to green tag, 1 to yellow tag and 0 to red tag.
def get_severity(req_params):
    if black_tag(req_params):
        return 3
    elif red_tag(req_params):
        return 0
    elif green_tag(req_params):
        return 2
    else:
        return 1


def black_tag(req_params):
    return not req_params["breathing"]


def red_tag(req_params):
    # I omitted the option of being red tagged for now because we may need a param to check if breathing twice
    b = req_params["breathing"]
    c = req_params["respiratory_rate"]
    d = req_params["perfusion"]
    e = req_params["capillary_refill"]
    f = req_params["can_obey_commands"]  # Responsive to commands or not
    # TODO: Maybe change logic based on each parameter so it could partially work without all parameters being available
    if b is None or c is None or d is None or e is None or f is None:
        return False
    return b and (c >= 30 or (c < 30 and ((not d and (e >= 2 or e < 2 and not f)) or (d and not f))))


def green_tag(req_params):
    return req_params["can_walk"]
