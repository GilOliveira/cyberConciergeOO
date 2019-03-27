# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo

from Match import Match
from ExpertsCollection import ExpertsCollection

def newFile(time, scope, company):
    """
    Opens a file in write mode and writes the required header in the first lines.
    Requires: time is DateTime
    Requires: company is str, the name of the company
    Requires: scope is str (must be either 'schedule' or 'experts').
    Ensures: the creation of a file with the required file name and header
    as stated in the project, the file is left open.
    """

    fileName = time.getYear()+'y'+time.getMonth()+'m'+ time.getDay() +\
               scope + time.getHour()+'h'+time.getMinute()+'.txt'
    file = open(fileName, 'w')
    file.writelines(['Day: \n', time.getDate(), '\n', 'Time: \n', time.getTime(),
                     '\n', 'Company: \n', company, '\n', scope.capitalize(), ': \n'])
    file.close()
    return fileName


def writeSchedule(fileName, schedule):
    """
    Opens a schedule file in append mode, adds the schedule from the collection,
    then closes the file.
    Requires: fileName as str (must be a schedule file)
    Requires: schedule as Schedule
    Ensures: A file with the schedule
    """
    file = open(fileName, 'a')
    file.writelines(schedule.outputSchedule())
    file.close()

def writeExperts(fileName, experts):
    """
    Opens a schedule file in append mode, adds the schedule from the collection,
    then closes the file.
    Requires: fileName as str (must be a experts file)
    Requires: experts as ExpertsCollection
    Ensures: A file with the updated list of experts.
    """
    file = open(fileName, 'a')
    experts.sortExperts()
    experts.writeExperts()
