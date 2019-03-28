# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo

from copy import deepcopy
from Match import Match

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
        list1 = []
        list2 = []

        for i in self.getList():
            if not i.getSuccess():
                list1.append(i)  # Denied list
                
            else:    
                list2.append(i)  # Matched list
        
        swapped = True
        k = len(list1)

        # Bubble sort algorithm - sorting by time (ascending)
        while k > 0 and swapped:
            for i in range(1, k):
                if list1[i - 1].getTime() > list1[i].getTime():
                    swapItem = list1[i]
                    list1[i] = list1[i - 1]
                    list1[i - 1] = swapItem
                    swapped = True
            k -= 1

        swapped = True
        k = len(list2)

        # Bubble sort algorithm - sorting by time (ascending)
        while k > 0 and swapped:
            for i in range(1, k):
                if list2[i - 1].getTime() > list2[i].getTime():
                    swapItem = list2[i]
                    list2[i] = list2[i - 1]
                    list2[i - 1] = swapItem
                    swapped = True
            k -= 1

        self.setList(list1+list2)

    def outputSchedule(self):
        """
        Creates a list to be outputted to the schedule file.
        Ensures: a list to be used in the writelines
        """

        outputList = []

        for i in self.getList():
            outputList.append(str(i) + '\n')

        return outputList

    def getList(self):
        """
        The collection as a list.
        Ensures: list of items in the collection
        """
        return deepcopy(self._matches)

    def setList(self, list):

        self._matches = list

    def items(self):
        """
        Iterates on the items of the collection.
        """
        for i in self.getList():
            yield i

    def __str__(self):
        """
        Manages the output
        Ensures: a string with all the items in the collection.
        """
        outStr = ""
        for i in self.getList():
            outStr = outStr + str(i) + "; "

    def __eq__(self, other):
        """
        Returns true if self and other have the same number
        of experts (but not necessarily the same ones)
        Requires: other is Schedule
        Ensures: a bool - True if both collections have the same
                length
        """
        if len(self.getList()) == len(other.getList()):
            return True
        else:
            return False

    def __lt__(self, other):
        """
        Returns True if other has more elements.
        Requires: other is Schedule
        Ensures: a bool - True other has more elements
        """
        if len(self.getList()) < len(other.getList()):
            return True
        else:
            return False
