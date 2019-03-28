class Duration:
    def __init__ (self, duration):
        """
        
        """
        self._hours = int (duration [0])
        self._minutes = int (duration [2:])
        
    def getHours (self):
        """
        """
        return self._hours
    
    def getMinutes (self):
        """
        """
        return self._minutes
    
    def setHours (self, hours):
        """
        """
        return self._hours
    
    def setMinutes (self, minutes):
        """
        """
        return self._minutes
    
    def floatHours (self):
        """
        """
        minTotal = (self._minutes + 60 * self._hours)
        
        return minTotal/60
    
    def items(self):
        """
        """

        for i in [self.getHours(),
                  self.getMinutes()]:
            yield i

    def __str__(self):
        """
     
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
        """
        if self.getHour() == other.getHour() and\
           self.getMinute() == other.getMinute():
            return True
        else:
            return False
        
