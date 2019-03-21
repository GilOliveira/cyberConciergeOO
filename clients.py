
# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo


class Clients:
    def __init__(self, name, zone, date, hour, max_hourly_charge, min_rating, required_expertise, duration):
        """
        Initializes a Client object
        Requires: name, zone as str
        Requires: required_expertise as tuple
        Requires: min_rating as int between 0 and 5
        Requires: max_hourly_charge, duration as float
        """
        self._name = name  # Client Name
        self._zone = zone  # Client zone
        self._date = date
        self._hour = hour
        self._max_hourly_charge = max_hourly_charge
        self._min_rating = min_rating
        self._required_expertise = required_expertise
        self._duration = duration

    def getName(self):
        """
        Returns the name of the client.
        Ensures: a str with the client's name.
        """
        return self._name

    def getZone(self):
        """
        Returns the zone of the client.
        Ensures: a str with the name of the zone.
        """
        return self._zone
    
       def getDate(self):
        """
        Returns date from whitch the request must be done.
        Ensures: a str with the requested date.
        """
        return self._date

    def getHour(self):
        """
        Returns hour from whitch the request must be done.
        Ensures: a str with the requested hour.
        """
        return self._hour

    def getMax_hourly_charge(self):
        """
        Returns the maximum accepted by the client to be charged per hour.
        Ensures: a float of the maximum accepted by the client to be charged per hour.
        """
        return self._max_hourly_charge

    def getMin_rating(self):
        """
        Returns the minimum rating of the expert accepted by the client.
        Ensures: an int between 0 and 5, the star rating of the expert.
        """
        return self._min_rating

    def getRequired_expertise(self):
        """
        Returns the expertise needed by the client.
        Ensures: a tuple expertise needed for the job.
        """
        return self._required_expertise

    def getDuration(self):
        """
        Returns the duration of the job required by the client.
        Ensures: a float with the duration of the job.
        """
        return self._duration

    def __str__(self):
        return str(self.getName()) + ', ' +\
               str(self.getZone()) + ', ' +\
               str(self.getDate()) + ', ' +\
               str(self.getHour()) + ', ' +\
               str(self.getMax_hourly_charge()) + ', ' +\
               str(self.getMin_rating()) + ', ' +\
               str(self.getRequired_expertise()) + ', ' +\
               str(self.getDuration())
