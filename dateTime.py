from constants import openingTime
from constants import closingTime
from constants import monthDays
from constants import hourMinutes
from constants import yearMonths


class dateTime:
    def __init__(self, year, month, day, hour, minute):
        """
        Initializes a dateTime object
        Requires: year, month, day, hour, minute as int
        """
        self._year = year
        self._month = month
        self._day = day
        self._hour = hour
        self._minute = minute
    
    def getYear(self):
        """
        Returns the year of the request.
        Ensures: an int with the year.
        """
        return self._year
    
    def getMonth(self):
        """
        Returns the month of the request.
        Ensures: an int with the month.
        """
        return self._month
    
    def getDay(self):
        """
        Returns the day of the request.
        Ensures: an int with the day.
        """
        return self._day
    
    def getHour(self):
        """
        Returns the hour of the request.
        Ensures: an int with the hour.
        """
        return self._hour
    
    def getMinute(self):
        """
        Returns the minute of the request.
        Ensures: an int with the minute.
        """
        return self._minute
    
    
    def __str__(self):
        return str(self.getYear()) + '-' +\
               str(self.getMonth()) + '-' +\
               str(self.getDay()) + ', ' +\
               str(self.getHour()) + ':' +\
               str(self.getMinute())
             
    def addTime(self, increment):
        """
        Returns the increment of the year, month, day, hour, minute.
        Ensures: an int with the increment of the year, month, day, hour, minute.
        """
        endYear = self.getYear()
        endMonth = self.getMonth()
        endDay = self.getDay()
        endHour = self.getHour()
        endMinute = self.getMinute() + increment
        
        if endMinute > hourMinutes - 1:
            endHours = endHour + endMinute // hourMinutes
            endMinutes = endMinute % hourMinutes

        while (endHours == closingTime and endMinutes > 0) or endHours > closingTime:
            endHours = openingTime + (endHours-closingTime)
            endDay += 1

        while endDay > monthDays:
            endDay = endDay - monthDays
            endMonth += 1

        while endMonth > yearMonths:
            endMonth = endMonth - yearMonths
            endYear += 1

        return str(self.endYear()) + '-' +\
               str(self.endMonth()) + '-' +\
               str(self.endDay()) + ', ' +\
               str(self.endHour()) + ':' +\
               str(self.endMinute())
