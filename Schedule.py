# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo


class Schedule:

    def __init__(self):
        """
        Creates a Schedule object - a collection of matches.
        """

        self._matches = []  # collection starts empty

    def addToSchedule(self, match):
        """
        Adds a new schedule entry to the collection.
        Requires: match is Match
        """

        self._matches.append(match)

    def sortSchedule(self):
        """
        Sorts the schedule in the correct output order.
        """

        pass

    def outputSchedule(self):
        """
        Creates a list to be outputted to the schedule file.

        """

        pass

    def __str__(self):
        """
        Manages the output
        """

        pass
