# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo


class Expert:
    def __init__(self, name, zone, skills, rating, rate, date, hour, earnings):
        """
        Initializes an Expert object
        Requires: name, zone as str
        Requires: skills as tuple
        Requires: rating as int between 0 and 5
        Requires: rate, earnings as float
        """
        self._name = name  # expert Name
        self._zone = zone  # working zone
        self._skills = skills
        self._rating = rating
        self._rate = rate
        self._date = date
        self._hour = hour
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

    def getDate(self):
        """
        Returns next available working date for the expert.
        Ensures: a str with the next available free date.
        """
        return self._date

    def getHour(self):
        """
        Returns next available working hour for the expert.
        Ensures: a str with the next available free hour.
        """
        return self._hour

    def getEarnings(self):
        """
        Returns the total earnings of the experts.
        Ensures: a float with the total expert earnings.
        """
        return self._earnings

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
               str(self.getDate()) + ', ' +\
               str(self.getHour()) + ', ' +\
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
