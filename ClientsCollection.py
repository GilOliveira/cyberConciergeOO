# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo

from Client import Client
from copy import deepcopy


class ClientsCollection:

    def __init__(self):
        """
        Creates a new ClientsCollection object,
        a collection of Client.
        The collection is created empty.
        """

        self._data = []

    def getClientsList(self):
        """
        Gets the list of clients
        Ensures: a List of clients
        """

        return deepcopy(self._data())

    def addClient(self, client):
        """
        Adds a new client to the collection.
        Requires: client is Client
        """
        self._data.append(client)

    def items(self):
        """
        Iterates on each of the clients.
        """

        for i in self.getClientsList():
            yield i

    def sortByRequestTime(self):
        """
        Rearranges the collection in order of
        request time.
        """
        pass

    def count(self):
        """
        Counts the number of clients in the collection.
        Ensures: an int with the number of clients
        """

        return len(self.getClientsList())

    def items(self):
        """
        Iterates each one of the Clients in the collection.
        """
        for i in self._data:
            yield i

    def __str__(self):
        """
        Returns a string of all entries of the collection.
        """
        return str(self.getClientsList())

    def __eq__(self, other):
        """
        Compares if both collections have the same number of items.
        Ensures: a bool, True if self and other have the same number of items.
        """
        if self.count() == other.count():
            return True

    def __lt__(self, other):
        """
        Number of item between collections.
        Ensures: a bool, True if self has less items than other.
        """
        if self.count() == other.count():
            return True
