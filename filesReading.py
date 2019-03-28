# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo

from Match import Match
from ExpertsCollection import ExpertsCollection
from DateTime import DateTime

def readnewFile(fileName):
    """
    Opens a file in read mode and reads the required header in the first lines.
    Requires: time is DateTime
    Requires: company is str, the name of the company
    Requires: scope is str (must be either 'schedule' or 'experts').
    Ensures: the reading of a file with the required file name and header
    as stated in the project.
    """

    file = open(fileName, 'r')
    file.readline()  # Ignore first line
    fullDate = file.readline()  # YYYY-MM-DD
    outDate =

    file.close()
    return fileName


def readSchedule(fileName, schedule):
    """
    Opens a schedule file in read mode.
    Requires: fileName as str (must be a schedule file)
    Requires: schedule as Schedule
    Ensures: reading a file with the schedule
    """
    file = open(fileName, 'a')
    file.readlines(schedule.outputSchedule())
    file.close()

def readExperts(fileName, experts):
    """
    Opens a experts file in read mode.
    Requires: fileName as str (must be a experts file)
    Requires: experts as ExpertsCollection
    Ensures: the reading of a file with the experts listing.
    """
    file = open(fileName, 'a')
    experts.sortExperts()
    experts.readExperts()