# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo

from Match import Match
from ExpertsCollection import ExpertsCollection
from DateTime import DateTime
from ClientsCollection import ClientsCollection
from Client import Client
from Duration import Duration
from Expert import Expert

def readNewFile(fileName):
    """
    Opens a file in read mode and reads the required header in the first lines.
    Requires: fileName is str, the name of the file to be opened
    Ensures: the reading of a file with the required file name and header
    as stated in the project, returning a tuple with:
            time is DateTime
            company is str, the name of the company
            scope is str (must be either 'schedule' or 'experts').
    """

    file = open(fileName, 'r')
    file.readline()  # Ignore first line
    fullDate = file.readline()  # YYYY-MM-DD
    file.readline()  # Ignore third line
    fullTime = file.readline()  #HH:MM
    timestamp = DateTime(
        int(fullDate[0:4]),
        int(fullDate[5:7]),
        int(fullDate[8:10]),
        int(fullTime[0:2]),
        int(fullTime[3:5]))
    file.readline()  # Ignore fifth line
    company = file.readline().replace("\n", "")
    scope = file.readline().replace("\n", "").replace(":", "")
    file.close()

    return (timestamp, company, scope)


def readClients(fileName):
    """
    Opens a client file in read mode.
    Requires: fileName as str (must be a client file)
    Ensures: inClients is ClientsCollection
    """
    fileIn = open(fileName, 'r')
    filetwo = open(fileName, 'r')
    lenfile = len(filetwo.readlines())

    outputList = []
    inClients = ClientsCollection()

    # header always has 7 lines
    for i in range(7):
        fileIn.readline()

    for i in range(lenfile - 7):
        outputList.append(fileIn.readline().replace("*", "").replace("\n", "").split(","))

    for i in outputList:

        #Calculate month
        if i[2][6] == '0':
            month = int(i[2][7])
        else:
            month = int(i[2][6:8])

        # Calculate day
        if i[2][9] == '0':
            day = int([2][10])
        else:
            day = int(i[2][-2:])

        # Calculate hour
        if i[3][1] == '0':
            hour = int(i[3][2])
        else:
            hour = int(i[3][1:3])

        # Calculate minute
        if i[3][4] == '0':
            minute = int(i[3][5])
        else:
            minute = int(i[3][4:6])

        clientTemp = Client(i[0],
                            i[1][1:],
                            DateTime(int(i[2][1:5]), month, day, hour, minute),
                            int(i[4][1:]),
                            int(i[5][1:]),
                            i[6][1:],
                            Duration(i[7][1:]))

        inClients.addClient(clientTemp)

    fileIn.close()
    filetwo.close()

    return inClients


def readExperts(fileName):
    """

    """
    fileIn = open(fileName, 'r')
    filetwo = open(fileName, 'r')
    lenfile = len(filetwo.readlines())

    outputList = []
    inExperts = ExpertsCollection()

    # header always has 7 lines
    for i in range(7):
        fileIn.readline()

    for i in range(lenfile - 7):
        outputList.append(fileIn.readline().replace("*", "").replace("\n", "").split(","))

    for i in outputList:

        # Calculate month
        if i[5][6] == '0':
            month = int(i[5][7])
        else:
            month = int(i[5][6:8])

        # Calculate day
        if i[5][9] == '0':
            day = int(i[5][10])
        else:
            day = int(i[5][9:11])

        # Calculate hour
        if i[6][1] == '0':
            hour = int(i[6][2])
        else:
            hour = int(i[6][1:3])

        # Calculate minute
        if i[6][4] == '0':
            minute = int(i[6][5])
        else:
            minute = int(i[6][4:6])

        expertTemp = Expert(i[0],
                            i[1][1:],
                            tuple(i[2][1:].replace(";",",").replace("(","").replace(")","").replace(" ","").split(",")),
                            int(i[3][1:]),
                            int(i[4][1:]),
                            DateTime(int(i[5][1:5]), month, day, hour, minute),
                            float(i[7][1:]))

        inExperts.addExpert(expertTemp)


    fileIn.close()
    filetwo.close()

    return inExperts
