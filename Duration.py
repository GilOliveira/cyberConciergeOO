class Duration:
    def __init__ (self, duration):
        """
        Creates a new object which stores a duration.
        Requires: str in which duration[0] is the hour
                  and duration [2:] are the minutes.
        """
        self._hours = int(duration[0])
        self._minutes = int(duration[2:])
        
    def getHours(self):
        """
        Gets the hours value.
        Ensures: an int with the hours value.
        """
        return self._hours
    
    def getMinutes(self):
        """
        Gets the minutes value.
        Ensures: an int with the minutes value.
        """
        return self._minutes
    
    def setHours(self, hours):
        """
        Sets the hours value.
        Requires: hours (as int)
        """
        return self._hours
    
    def setMinutes(self, minutes):
        """
        Sets the minutes value.
        Requires: minutes (as int).
        """
        return self._minutes

    def getTotalMinutes(self):
        """
        Converts hours:minutes into minutes - int
        Ensures: an int, the amount of minutes in duration
        """
        return self._minutes + 60 * self._hours
    
    def floatHours(self):
        """
        Converts hours:minutes into decimal
        Ensures: a float, the amount of hours in duration
        """
        
        return self.getTotalMinutes()/60
    
    def items(self):
        """
        Iterator: first yields hours, then minutes
        """

        for i in [self.getHours(),
                  self.getMinutes()]:
            yield i

    def __str__(self):
        """
        Generates a str in the 0h00 format
        Ensures: a str with the duration.
        """

        hoursStr = str(self.getHours())
        minutesStr = str(self.getMinutes())

        if self.getHours() < 10:
            hoursStr = '0' + hoursStr

        if self.getMinutes() < 10:
            minutesStr = '0' + minutesStr

        return str(hoursStr + 'h'+\
               minutesStr)

    def __lt__(self, other):
        """
        Compares two durations.
        Ensures: a bool, True if self is less time than other
        """
        selfNumeric = self.getHours()*100 +\
                      self.getMinutes()

        otherNumeric = other.getHours()*100 +\
                       other.getMinutes()

        if selfNumeric < otherNumeric:
            return True
        else:
            return False

    def __eq__(self, other):
        """
        Compares two durations.
        Ensures: a bool, True if both durations are the same.
        """
        if self.getHour() == other.getHour() and\
           self.getMinute() == other.getMinute():
            return True
        else:
            return False
