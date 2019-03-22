# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo


class Match:
    def __init__(self, success, time, client, expert):
        """
        Initiates a new Match object.
        Requires: success as bool (False if declined)
        Requires: client as Client.
        Requires: expert as Expert.
        Ensures: The creation of a new object with
                 two attributes, client and expert.
        """

        self._success = success
        self._client = client
        self._expert = expert
        self._time = time

    def getClient(self):
        """
        Returns the client.
        Ensures: client as Client.
        """

        return self._client

    def getExpert(self):
        """
        Returns the expert.
        Ensures: expert as Expert.
        """

        return self._expert

    def setClient(self, client):
        """
        Sets the client.
        Requires: client is Client
        """

        self._client = client

    def setExpert(self, expert):
        """
        Sets the expert.
        Requires: expert is Expert.
        """

        self._expert = expert

    def setTime(self, time):
        """
        Sets the match time.
        Requires: time is DateTime
        """

        self._time = time

    def getTime(self):
        """
        Gets the match time as DateTime.
        """

        return self._time

    def getSuccess(self):
        """
        Returns True if match was successful,
        False if declined.
        """

        return self._success

    def setSuccess(self, success):
        """
        Sets the success attribute.
        Requires: success as bool
        """

        self._success = success

    def __str__(self):
        """
        Returns a string in the format to be written
        in the schedule.
        """

        if self.getSuccess():
            return str(self.setTime()) + ', ' +\

