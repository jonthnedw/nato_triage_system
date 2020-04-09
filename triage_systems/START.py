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


class Start:
    def __init__(self, person):
        # Dictionary of each param mapping to the value
        self.req_params = REQUIRED_PARAMS.copy()
        self.person = person
        self.severity = ""
        self.update_req_params()

    def update_req_params(self):
        for param in self.req_params.keys():
            self.req_params[param] = self.person.get_data(param)

    def get_req_params(self):
        return self.req_params

    def update_severity(self):
        if self.black_tag():
            self.severity = "black"
        elif self.red_tag():
            self.severity = "red"
        # I slighty modified the algorithm so that if you can walk but also show possible signs
        # of a red tag you'll get red tagged as opposed to green tag. This can change by changing
        # the order of if statements
        elif self.green_tag():
            self.severity = "green"
        else:
            self.severity = "yellow"

    def get_severity(self):
        return self.severity
    # underlying green tag equation, g(a,b,c,d,e,f) = a
    # green tag if they can walk
    def green_tag(self):
        return self.req_params["can_walk"]

    # underlying black tag equation, b(a,b,c,d,e,f) = !b
    # black tag if not breathing
    def black_tag(self):
        return not self.req_params["breathing"]

    """underlying red tag equation
     r(a,b,c,d,e,f) = b && (c >= 30 || (c < 30 && (d && (e >= 2 || e < 2 && !f)) || (!d && !f))))
    """

    def red_tag(self):
        # I omitted the option of being red tagged for now because we may need a param to check if breathing twice
        b = self.req_params["breathing"]
        c = self.req_params["respiratory_rate"]
        d = self.req_params["perfusion"]
        e = self.req_params["capillary_refill"]
        f = self.req_params["can_obey_commands"]  # Responsive to commands or not
        return b and (c >= 30 or (c < 30 and ((not d and (e >= 2 or e < 2 and not f)) or (d and not f))))

    # No yellow tag because if you are neither black, red or green tagged then you are yellow tagged.
    # TODO add condtionds for when a param is not preesent
