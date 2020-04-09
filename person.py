class Person:
    """
    Person class that will hold all user-entered parameters that triage systems can request.
    TODO Rewrite description in terms of MVC
    TODO Design additional methods
    TODO Implement additional methods
    """
    def __init__(self, params):
        self.params = params

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
