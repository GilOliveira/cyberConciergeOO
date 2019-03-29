# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo


class Client:
    def __init__(self, name, zone, dateTime, max_hourly_charge, min_rating, required_expertise, duration):
        """
        Initializes a Client object
        Requires: name, zone as str
        Requires: required_expertise as tuple
        Requires: min_rating as int between 0 and 5
        Requires: max_hourly_charge, duration as float
        """
        self._name = name
        self._zone = zone
        self._dateTime = dateTime
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

    def getDateTime(self):
        """
        """
        return self._dateTime


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
    
    
    def setName(self, name):
        """
        Sets the name of the Client.
        Requires: name (is str)
        """
        self._name = name

    def setZone(self, zone):
        """
        Sets the zone of the Client.
        Requires: zone (is str)
        """
        self._zone = zone

    def setdateTime(self, dateTime):
        """
        Sets the dateTime of the Client.
        Requires: dateTime (is dateTime)
        """
        self._dateTime = dateTime


    def setMax_hourly_charge(self, max_hourly_charge):
        """
        Sets the max hourly charge the client accepts.
        Requires: max_hourly_charge (is int)
        """
        self._max_hourly_charge = max_hourly_charge

    def setMin_rating(self, min_rating):
        """
        Sets the minimum rating the client accepts.
        Requires: min_rating (is int)
        """
        self._min_rating = min_rating

    def setRequired_expertise(self, required_expertise):
        """
        Sets the skill required for the job.
        Requires: required_expertise (is str)
        """
        self._required_expertise = required_expertise

    def setDuration(self, duration):
        """
        Sets the duration of the job.
        Requires: duration (is duration)
        """
        self._duration = duration

    def items (self):
        """
        Iterates over the various attributes of client.
        Name, Zone, DateTime, Max Charge, Max Rating, Required Skill, Duration
        """
        for i in [self.getName(),
              self.getZone(),
              self.getDateTime(),
              self.getMax_hourly_charge(),
              self.getMin_rating(),
              self.getRequired_expertise(),
              self.getDuration()]:
            yield i

    def __str__(self):
        """
        Sets the string output with all the attributes.
        """
        return str(self.getName()) + ', ' +\
               str(self.getZone()) + ', ' +\
               str(self.getDateTime()) + ', ' +\
               str(self.getMax_hourly_charge()) + ', ' +\
               str(self.getMin_rating()) + '*, ' +\
               str(self.getRequired_expertise()) + ', ' +\
               str(self.getDuration())
               
    def __eq__(self, other):
        """
        Compares Client timestamps.
        Ensures: A bool, True if self and other have the same dateTime.
        """
        if self.getDateTime() == other.getdateTime():
            return True

    def __lt__ (self, other):
        """
        Compares Client timestamps.
        Ensures: A bool, True if self's dateTime is before other.
        """
        if self.getDateTime() < other.getdateTime():
            return True
