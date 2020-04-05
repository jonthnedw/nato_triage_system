"""
This file contains all functions needed to perform a START triage based on the findings at:
https://chemm.nlm.nih.gov/startadult.htm
"""
from triage_systems import TriageSystemAbstract

LIST_OF_QUESTIONS = [
    ("Able to walk?", bool),
    ("Does individual have spontaneous breathing?", bool),
    ("What is their respiratory rate?", int),
    ("What is their perfusion?", int),
    ("What is their mental status?", bool)
]


def get_questions():
    return LIST_OF_QUESTIONS


def quantify_vector(vector):
    # TODO: Write code that returns an int based on the vector response of the individual
    return -1


class StartSystem:
    # TODO Maybe we'll use System objects ¯\_(ツ)_/¯
    pass
