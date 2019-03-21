# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo

from copy import deepcopy


class ExpertsCollection:

    def __init__(self):
        """
        Initiates a collection of experts.
        """

        self._data = []

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

    def items(self):
        """
        Iterates on each of the Experts
        """

        for i in self.getExpertsList():
            yield i

    def setCriteria(self, rating, hourlyRate, zone):
        """
        Excludes unfit Experts with the given criteria.
        Requires: rating (int), the minimum rating accepted
        Requires: hourlyRate (int), the max rate the client is
                  willing to pay
        Requires: zone (str), the working zone
        Ensures: the removal of the Experts who don't fit the´
                 criteria from the collection
        """

        for i in range(len(self._data)):
            if self._data[i].getZone() != zone \
                    or self._data[i].getRating() < rating \
                    or self._data[i].getRate() > hourlyRate:

                self._data.pop(i)

    def bestExpert(self):
        """
        Returns the best expert, according to the project criteria.
        Ensures: the best expert (as Expert) of a collection of
                 compatible experts.
        """
        pass


