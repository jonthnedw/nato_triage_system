"""
The intention for this file is to have an abstract class where all triage systems inherit just to make running a
script more easier
"""
from abc import ABC, abstractmethod


class TriageSystemAbstract(ABC):

    """
    Each system should have a series of questions or information needed from the injured in-order to perform triage.
    This method likewise returns a list of tuples where each tuples contains a string of the question and the base type
    the response should be (ie. int, bool, ect.)
    """
    @abstractmethod
    def get_questions(self):
        pass

    @abstractmethod
    def quantify_vector(self):
        pass