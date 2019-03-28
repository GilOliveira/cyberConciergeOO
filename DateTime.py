from constants import openingTime
from constants import closingTime
from constants import monthDays
from constants import hourMinutes
from constants import yearMonths


class DateTime:
    def __init__(self, year, month, day, hour, minute):
        """
        Initializes a dateTime object - functions as a timestamp.
        Requires: year, month, day, hour, minute as int
        """
        self._year = year
        self._month = month
        self._day = day
        self._hour = hour
        self._minute = minute
  
    def setYear(self, year):
       self._year = year
    
    def setMonth(self, month):
       self._month = month
    
    def setDay(self, day):
       self._day = day
    
    def setHour(self, hour):
       self._hour = hour
    
    def setMinute(self, minute):
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

             
    def addTime(self, increment):
        """
        Returns the increment of the year, month, day, hour, minute.
        Requires: increment (int), the amount of minutes to be added
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

    def items(self):
        """
        Iterates over the different parameters of the timestamp.
        """

        for i in [self.getYear(),
                  self.getMonth(),
                  self.getDay(),
                  self.getHour(),
                  self.getMinute()]:
            yield i

    def __str__(self):
        """
        Returns a string with the object date and time.
        Ensures: an str with fixed number of characters
                 in 'YYYY-MM-DD, HH:MM' format
        """

        monthStr = str(self.getMonth())
        dayStr = str(self.getDay())
        hourStr = str(self.getHour())
        minuteStr = str(self.getMinute())

        if self.getMonth() < 10:
            monthStr = '0' + monthStr

        if self.getDay() < 10:
            dayStr = '0' + dayStr

        if self.getHour() < 10:
            hourStr = '0' + hourStr

        if self.getMinute() < 10:
            minuteStr = '0' + minuteStr

        return str(self.getYear()) + '-' +\
               monthStr + '-' +\
               dayStr + ', ' +\
               hourStr + ':' +\
               minuteStr

    def __lt__(self, other):
        """
        Overrides < operator, comparing if one date
        is older than the other.
        Ensures: bool, True if date is older then other.
        """
        selfNumeric = self.getYear()*100000000 +\
                      self.getMonth()*1000000 +\
                      self.getDay()*10000 +\
                      self.getHour()*100 +\
                      self.getMinute()

        otherNumeric = other.getYear()*100000000 +\
                       other.getMonth()*1000000 +\
                       other.getDay()*10000 +\
                       other.getHour()*100 +\
                       other.getMinute()

        if selfNumeric < otherNumeric:
            return True
        else:
            return False

    def __eq__(self, other):
        """
        Overrides == operator, comparing if one timestamp
        is the same as the other.
        Ensures: bool, True both timestamps are the same.
        """
        if self.getYear() == other.getYear() and\
            self.getMonth() == other.getMonth() and\
            self.getDay() == other.getDay() and\
            self.getHour() == other.getHour() and\
            self.getMinute() == other.getMinute():
            return True
        else:
            return False
