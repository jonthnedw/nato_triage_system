from triage_systems.Start import Start
from person import Person


def main():
    p = Person({
        "can_walk": None,  # boolean value
        "breathing": None,  # boolean value
        "respiratory_rate": None,  # integer value
        "perfusion": None,  # (Radial pulse present), boolean value
        "capillary_refill": None,  # (In seconds) integer value
        "can_obey_commands": None  # boolean value
    }
    )
    system = Start(p)
    # You can mess around with inputs
    p.put_data("can_walk", False)
    p.put_data("breathing", True)
    p.put_data("respiratory_rate", 29)
    p.put_data("perfusion", True)
    p.put_data("capillary_refill", 1)
    p.put_data("can_obey_commands", True)
    system.update_req_params()
    system.update_severity()
    print(system.get_severity())

if __name__ == "__main__":
    main()