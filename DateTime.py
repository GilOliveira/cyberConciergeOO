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

    def getDate(self):

        monthStr = str(self.getMonth())
        dayStr = str(self.getDay())

        if self.getMonth() < 10:
            monthStr = '0' + monthStr

        if self.getDay() < 10:
            dayStr = '0' + dayStr

        return str(str(self.getYear()) + '-' +
                   monthStr + '-' + dayStr)

    def getTime(self):

        hourStr = str(self.getHour())
        minuteStr = str(self.getMinute())

        if self.getHour() < 10:
            hourStr = '0' + hourStr

        if self.getMinute() < 10:
            minuteStr = '0' + minuteStr

        return hourStr + ':' + minuteStr

  
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

    def getTitleDate(self):

        monthStr = str(self.getMonth())
        dayStr = str(self.getDay())

        if self.getMonth() < 10:
            monthStr = '0' + monthStr

        if self.getDay() < 10:
            dayStr = '0' + dayStr

        return str(self.getYear()) + 'y' + monthStr + 'm' + dayStr

    def getTitleHours(self):

        hourStr = str(self.getHour())
        minuteStr = str(self.getMinute())

        if self.getHour() < 10:
            hourStr = '0' + hourStr

        if self.getMinute() < 10:
            minuteStr = '0' + minuteStr

        return hourStr + 'h' + minuteStr
             
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
        endMinute = self.getMinute() + int(increment)
        
        if endMinute > hourMinutes - 1:
            endHour = endHour + endMinute // hourMinutes
            endMinute = endMinute % hourMinutes

        while (endHour == closingTime and endMinute > 0) or endHour > closingTime:
            endHour = openingTime + (endHour-closingTime)
            endDay += 1

        while endDay > monthDays:
            endDay = endDay - monthDays
            endMonth += 1

        while endMonth > yearMonths:
            endMonth = endMonth - yearMonths
            endYear += 1

        self.setYear(endYear)
        self.setMonth(endMonth)
        self.setDay(endDay)
        self.setHour(endHour)
        self.setMinute(endMinute)

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

        return self.getDate() + ', ' + self.getTime()

    def __lt__(self, other):
        """
        Overrides < operator, comparing if one date
        is older than the other.
        Ensures: bool, True if date is older then other.
        """

        # Converting the time into int in the format YYYYMMDDhhmm

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
