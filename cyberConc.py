# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo

import sys
from ExpertsCollection import ExpertsCollection
from ClientsCollection import ClientsCollection
import scheduling
import filesWriting
from DateTime import DateTime
import filesReading

def checkErrors(fileNameExperts, fileNameClients):
    """Checks to see if the inputFiles are valid. Checks if the headers of the experts
    and clients files are equal and if the header of a file matches its name
    Requires: fileNameExperts, fileNameClients are str, with the names
    of the files representing the list of experts and clients, respectively,
    following the format indicated in the project.
    Ensures: return True if the files are valid and False if not"""

    fileOK = True

    # Tests if the clients match between Client and Expert
    expInfo = filesReading.readNewFile(fileNameExperts)
    cliInfo = filesReading.readNewFile(fileNameClients)
    if expInfo[0] != cliInfo[0] or expInfo[1] != cliInfo[1]:
        print("Error in input files: inconsistent files",
              fileNameExperts, "and", fileNameClients)
        fileOK = False


    # tests if the header matches the file name
    # ex:2019y03m20clients12h30.txt = ('2019-02-20', '12:30', 'iCageDoree', 'Clients')   <<< deve dar erro neste exemplo

    fileOK = True

    if int(fileNameExperts[0:4]) != expInfo[0].getYear() or\
            int(fileNameExperts[5:7]) != expInfo[0].getMonth() or\
            int(fileNameExperts[8:10]) != expInfo[0].getDay() or\
            int(fileNameExperts[17:19]) != expInfo[0].getHour() or\
            int(fileNameExperts[20:22]) != expInfo[0].getMinute():
        print("Error in input file: inconsistent name and header in file", fileNameExperts)
        fileOK = False

    if int(fileNameClients[0:4]) != cliInfo[0].getYear() or\
            int(fileNameClients[5:7]) != cliInfo[0].getMonth() or\
            int(fileNameClients[8:10]) != cliInfo[0].getDay() or\
            int(fileNameClients[17:19]) != cliInfo[0].getHour() or\
            int(fileNameClients[20:22]) != cliInfo[0].getMinute():
        print("Error in input file: inconsistent name and header in file", fileNameClients)
        fileOK = False


    return fileOK

def assign(inputExperts, inputClients):
    """
    Assigns the given experts to the given clients.
    Requires: inputExperts (is ExpertsCollection)
    Requires: inputClients (is ClientsCollection)
    """
    fileInfo = filesReading.readNewFile(inputExperts)

    scheduleTime = fileInfo[0]
    scheduleTime.addTime(30)

    company = fileInfo[1]

    inExperts = filesReading.readExperts(inputExperts)
    inRequests = filesReading.readClients(inputClients)

    outScheduling = scheduling.update(inRequests, inExperts, scheduleTime)

    newSchedule = outScheduling[0]
    newExperts = outScheduling[1]


    scheduleName = filesWriting.newFile(scheduleTime, 'schedule', company)
    filesWriting.writeSchedule(scheduleName, newSchedule)

    expertsName = filesWriting.newFile(scheduleTime, 'experts', company)
    filesWriting.writeExperts(expertsName, newExperts)

# ---- PROGRAM STARTS RUNNING HERE -------

inputExperts, inputClients = sys.argv[1:]

if checkErrors(inputExperts, inputClients): 
   
    assign(inputExperts, inputClients)

