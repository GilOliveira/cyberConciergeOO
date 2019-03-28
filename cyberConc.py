# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo

import sys
from ExpertsCollection import ExpertsCollection
from ClientsCollection import ClientsCollection
import scheduling
import filesWriting
from DateTime import dateTime

def assign(inputExperts, inputClients):

    # COLOCAR CÓDIGO QUE CHAME O FILES READING AQUI
    # OS INPUTS DEVERÃO SER INSERIDOS EM inRequests e inExperts
    # TAMBÉM É NECESSÁRIO TER O scheduleTime e o company

    outScheduling = scheduling.update(inRequests, inExperts)

    newSchedule = outScheduling[0]
    newExperts = outScheduling[1]

    scheduleTime.addTime(30)
    scheduleName = filesWriting.newFile(scheduleTime, 'schedule', company)
    filesWriting.writeSchedule(scheduleName, newSchedule)

    expertsName = filesWriting.newFile(scheduleTime, 'experts', company)
    filesWriting.writeExperts(expertsName, newExperts)

# ---- PROGRAM STARTS RUNNING HERE -------

inputExperts, inputClients = sys.argv[1:]

if True:  # SUBSTITUIR COM CHECK ERROS
    assign(inputExperts, inputClients)
