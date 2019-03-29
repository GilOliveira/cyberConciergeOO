# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo

from copy import deepcopy
from Expert import Expert


class ExpertsCollection:

    def __init__(self, data=[]):
        """
        Initiates a collection of experts.
        """

        self._data = data

    def addExpert(self, expert):
        """
        Adds a expert to the collection.
        Requires: expert is Expert
        """

        self._data.append(expert)

    def getExpertsList(self):
        """
        Gets the experts list.
        Ensures: list of Expert items.
        """

        return deepcopy(self._data)

    def setExpertsList(self, experts):
        """
        Sets the experts list.
        Requires: experts is list and is made up of
                  Expert objects.
        """

        self._data = experts

    def items(self):
        """
        Iterates on each of the Experts
        """

        for i in self.getExpertsList():
            yield i

    def setCriteria(self, rating, hourlyRate, zone, skill):
        """
        Excludes unfit Experts with the given criteria.
        Requires: rating (int), the minimum rating accepted
        Requires: hourlyRate (int), the max rate the client is
                  willing to pay
        Requires: zone (str), the working zone
        Ensures: the removal of the Experts who don't fit the´
                 criteria from the collection
        """

        compatibleExperts = []


        for i in range(self.count()):
            if self.getExpertsList()[i].getZone() == zone \
                    and self.getExpertsList()[i].getRating() >= rating \
                    and self.getExpertsList()[i].getRate() <= hourlyRate\
                    and skill in self.getExpertsList()[i].getSkills():
                compatibleExperts.append(self.getExpertsList()[i])

        self.setExpertsList(compatibleExperts)


    def bestExpert(self):
        """
        Returns the best expert, according to the project criteria.
        Ensures: the best expert (as Expert) of a collection of
                 compatible experts.
        """
        best = self.getExpertsList()[0]  # the best expert starts beeing the first

        # the following cycle will check who is the most suitable expert, by comparing
        # each expert to the 'best', in which case, the 'best' variable is updated
        for j in range(1, self.count()):
            # who is available first:
            if self.getExpertsList()[j].getDateTime() < best.getDateTime():
                best = self.getExpertsList()[j]
            elif self.getExpertsList()[j].getDateTime() == best.getDateTime():
                # who has the best rate:
                if self.getExpertsList()[j].getRate() < best.getRate():
                    best = self.getExpertsList()[j]
                elif self.getExpertsList()[j].getRate() == best.getRate():
                    # who has the least total earnings
                    if self.getExpertsList()[j].getEarnings() < best.getEarnings():
                        best = self.getExpertsList()[j]
                    elif self.getExpertsList()[j].getEarnings() == best.getEarnings():
                        # who is the first in alphabetical order:
                        if self.getExpertsList()[j].getName() < best.getName():
                            best = self.getExpertsList()[j]

        return best

    def sortExpertsByTime(self):
        """
        Sorts the experts by time of availability.
        """

        expList = self._data

        swapped = True
        k = len(expList)

        while k > 0 and swapped:
            for i in range(1, k):
                if expList[i-1].getDateTime() > expList[i].getDateTime():
                    swapItem = expList[i]
                    expList[i] = expList[i-1]
                    expList[i-1] = swapItem
                    swapped = True
            k -= 1

        self.setExpertsList(expList)

    def outputData(self):
        """
        Returns a list to be outputted into an updated experts file.
        """
        outputList = []
        for i in self._data:
            outputList.append(str(i) + ' \n')

        return outputList


    def count(self):
        """
        Returns how many experts are in the collection
        Ensures: an int, with the number of experts in the collection.
        """

        return len(self.getExpertsList())

    def updateMatchedExpert(self, name, newTime, earned):
        """
        Searches for the Expert using name, updates the time
        with newTime, and adds earned to the earnings.
        This method is meant to be used after a match, in order to
        update the expert's time and earnings after an appointment.
        Requires: name (str) must already exist in collection, the name
                  of the expert that will be updated
        Requires: newTime (dateTime), the new time of availability
        Requires: earned (int), the amount to be added to total earnings.
        """

        for i in self._data:
            if i.getName() == name:
                i.setEarnings(i.getEarnings() + earned)
                i.setDateTime(newTime)

    def __str__(self):

        strOut = ""
        for i in self.getExpertsList():
            strOut = strOut + str(i) + '; '
        return strOut

    def addTravelTime(self):
        """
        Add travel time (60 min.) to all experts in the collection
        """

        expertsList = self.getExpertsList()

        for i in range(len(self.getExpertsList())):
            self._data[i].addTravelTime()
