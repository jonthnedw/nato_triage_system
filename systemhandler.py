from pkgutil import walk_packages
import triage_systems
from person import Person

"""
System handler that's responsible for initializing the link between systems are persons. System handler uses a
publisher-subscriber pattern to notify systems that a parameter they monitor has changed. We use the terminology
of an event to talk about parameters being changed.
"""

# Dynamically loads all modules in the triage_systems package so we can notify each system of updated parameters
# Note that modules is a list of actual module objects, not of just module names
modules = []
for loader, name, is_pkg in walk_packages(triage_systems.__path__):
    modules.append(loader.find_module(name).load_module(name))


class Publisher:
    def __init__(self, params):
        self.events = {event: set() for event in params}  # Maps events to sets of subscriber modules

    def get_subscribers(self, event):
        return self.events[event]

    def register(self, event, who):
        try:
            self.get_subscribers(event).add(who)
        except KeyError:
            print(f"Invalid parameter: {event}")

    def notify(self, person, event):
        subscribers = self.get_subscribers(event)
        for subscriber in subscribers:
            subscriber.update(person)

    def setup(self):
        print("Initializing triage systems...")
        for module in modules:
            try:
                events = module.subscribe()  # events should be a list of params
                for event in events:
                    self.register(event, module)

            except AttributeError as e:
                print(f"No subscribe() function found in {module.__name__}.py")

if __name__ == '__main__':
    params = {
        "heart_rate": None,
        "blood_pressure": None
    }
    publisher = Publisher(params)
    publisher.setup()
    person = Person(params)
    publisher.notify(person, "heart_rate")