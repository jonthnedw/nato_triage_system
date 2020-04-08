import view
from person import Person

"""
This is the controller.
TODO Write about the controller
TODO Design controller methods
TODO Implement controller methods
"""

person = Person()


def update_parameter(parameter, value):
    person.put_data(parameter, value)
    print(person.params)
    # TODO: systems need to be informed that vitals have changed


def main():
    view.display()


if __name__ == "__main__":
    main()