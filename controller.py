import view
import systemhandler
from person import Person

"""
This is the controller.
TODO Write about the controller
TODO Design controller methods
TODO Implement controller methods
"""


def get_params():
    params = {}
    filepath = "params.txt"
    with open(filepath) as fp:
        for line in fp:
            if "#" in line:
                continue
            params[line.strip()] = None  # Read each param in params.txt and initialize to None
    return params


# TODO: modify this info chain to accept multiple persons
def update_parameter(person, parameter, value):
    person.put_data(parameter, value)
    publisher.notify(person, parameter)


# really bad interface for the view while we only support one person
def gui_socket(parameter, value):
    update_parameter(person, parameter, value)


params = get_params()
person = Person(params)  # Eventually delete this when we support creation of multiple persons
publisher = systemhandler.Publisher(params)
def main():
    # publisher.register("heart_rate", "Alice")
    # publisher.register("heart_rate", "Bob")
    # publisher.register("hr", "Charlie")
    publisher.setup()
    view.display()

if __name__ == "__main__":
    main()
    # TODO: fix the bug where the threading breaks the publisher :(
