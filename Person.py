class Person:
    """Person class that will hold all user-entered parameters that triage systems can request."""
    def __init__(self):
        self.params = {}
        filepath = "params.txt"
        with open(filepath) as fp:
            for line in fp:
                if "#" in line:
                    continue
                self.params[line.strip()] = None

    # Returns data to calling system
    def get_data(self, key):
        return self.params.get(key)

    # Inserts data into the params dictionary
    def put_data(self, key, value):
        try:
            if key in self.params:
                self.params[key] = value
            else:
                raise AttributeError
        except AttributeError:
            print(f"Invalid parameter: {key}")
