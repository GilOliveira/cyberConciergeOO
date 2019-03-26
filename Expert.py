# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo

from dateTime import dateTime

class Expert:
    def __init__(self, name, zone, skills, rating, rate, time, earnings):
        """
        Initializes an Expert object
        Requires: name, zone as str
        Requires: skills as tuple
        Requires: rating as int between 0 and 5
        Requires: rate, earnings as float
        Requires: time is DateTime
        """
        self._name = name  # expert Name
        self._zone = zone  # working zone
        self._skills = skills
        self._rating = rating
        self._rate = rate
        self._time = time
        self._earnings = earnings

    def getName(self):
        """
        Returns the name of the expert.
        Ensures: a str with the expert's name.
        """
        return self._name

    def getZone(self):
        """
        Returns the zone of the expert.
        Ensures: a str with the name of the zone.
        """
        return self._zone

    def getSkills(self):
        """
        Returns the skills of the expert.
        Ensures: a tuple of skills.
        """
        return self._skills

    def getRating(self):
        """
        Returns the zone of the expert.
        Ensures: an int between 0 and 5, the star rating of the expert.
        """
        return self._rating

    def getRate(self):
        """
        Returns the hourly rate of the expert.
        Ensures: a float with the hourly rate.
        """
        return self._rate

    def getTime(self):
        """
        Returns next available working time for the expert.
        Ensures: a DateTime with the next available free time.
        """
        return self._time

    def getEarnings(self):
        """
        Returns the total earnings of the experts.
        Ensures: a float with the total expert earnings.
        """
        return self._earnings

    def setEarnings(self, earnings):
        """
        Sets the earnings of the expert.
        Requires: earnings (int)
        """

        self._earnings = earnings

    def setTime(self, time):
        """
        Sets the next available time of the expert.
        Requires: time (dateTime)
        """

        self._time = time

    def addTravelTime(self):
        """
        Adds the travel time (60 min.) to the time attribute.
        If it exceeds the closing time, it sets 'time' to the
        next day at opening time.
        """

        self._time.addTime(60)

        if self._time.getHour == 8:
            self._time.setMinute == 0

    def __str__(self):
        """
        Overrides the string method.
        Ensures: an str, in the format to be outputted to the experts file:
        with name, zone, skills, rating, hourly rate and total earnings.
        """

        return str(self.getName()) + ', ' +\
               str(self.getZone()) + ', ' +\
               str(self.getSkills()) + ', ' +\
               str(self.getRating()) + '*, ' +\
               str(self.getRate()) + ', ' +\
               str(self.getTime()) + ', ' +\
               str(self.getEarnings())

    def __eq__(self, other):
        """
        Overrides the equals (==) operator
        """
        return self.getRating() == other.getRating()

    def __lt__(self, other):
        """
        Overrides the less than (<) operator
        """
        return self.getRating() < other.getRating()
