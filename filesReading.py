from Match import Match
from ExpertsCollection import ExpertsCollection
from ClientsCollection import ClientsCollection

def readFile(fileName):
    """
    Converts a given file listing experts or clients into a collection
    Requires: fileName is str, the name of a .txt file listing experts,
    following the format specified in the project.
    Ensures: class whose first element is the first expert or client and its resume up until the last expert
    """

    fileIn = open(fileName, 'r')
    filetwo = open(fileName, 'r')
    lenfile = len(filetwo.readlines())
    
    outputList = []

    # header always has 7 lines
    for i in range(7):
        fileIn.readline()

    for i in range(lenfile-7):
        outputList.append(fileIn.readline().replace("*","").replace("\n","").split(","))

    return outputList


def readHeader(fileName):
    """
    Converts a given file listing experts or clients and returns day, time,
    company as variables.
    Requires : fileName is str, the name of a .txt file listing experts,
    following the format specified in the project.
    Ensures: class with day, time, company and scope as str
    """

    fileIn = open(fileName, 'r')

    fileIn.readline()
    day = fileIn.readline().replace("\n", "")
    fileIn.readline()
    time = fileIn.readline().replace("\n", "")
    fileIn.readline()
    company = fileIn.readline().replace("\n", "")
    scope = fileIn.readline().replace("\n", "").replace(":","")
    return (day,time,company,scope)





