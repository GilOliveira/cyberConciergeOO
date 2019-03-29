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


def assign(inputExperts, inputClients):

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

if True:  # SUBSTITUIR COM CHECK ERROS
    assign(inputExperts, inputClients)
