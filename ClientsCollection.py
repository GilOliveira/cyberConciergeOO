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
        for i in self._data:
            yield i

    def __str__(self):
        return str(self._data)

