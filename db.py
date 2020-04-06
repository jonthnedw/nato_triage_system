class Database:
    """Database class that will hold all user-entered parameters that triage systems can request."""
    def __init__(self):
        self.params = {}

    # Returns data to calling system
    def get_data(self, label):
        return self.params.get(label)

    # TODO maybe check to make sure label is an accepted param label
    # Inserts data into the params dictionary
    def put_data(self, label, data):
        self.params[label] = data
