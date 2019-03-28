# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo

from DateTime import DateTime

class Expert:
    def __init__(self, name, zone, skills, rating, rate, dateTime, earnings):
        """
        Initializes an Expert object
        Requires: name, zone as str
        Requires: skills as tuple
        Requires: rating as int between 0 and 5
        Requires: rate, earnings as float
        Requires: dateTime is DateTime
        """
        self._name = name  # expert Name
        self._zone = zone  # working zone
        self._skills = skills
        self._rating = rating
        self._rate = rate
        self._dateTime = dateTime
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

    def getDateTime(self):
        """
        Returns next available working time for the expert.
        Ensures: a DateTime with the next available free time.
        """
        return self._dateTime

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

    def setDateTime(self, dateTime):
        """
        Sets the next available time of the expert.
        Requires: dateTime (dateTime)
        """

        self._dateTime = dateTime

    def addTravelTime(self):
        """
        Adds the travel time (60 min.) to the dateTime attribute.
        If it exceeds the closing time, it sets 'dateTime' to the
        next day at opening time.
        """

        dateTime = self.getDateTime()
        dateTime.addTime(60)

        if dateTime.getHour() == 8:
            dateTime.setMinute(0)

        self.setDateTime(dateTime)

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
               str(self.getDateTime()) + ', ' +\
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
