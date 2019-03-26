# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo

from copy import deepcopy
from ExpertsCollection import ExpertsCollection
from ClientsCollection import ClientsCollection
from Match import Match
from Expert import Expert
from Schedule import Schedule

def update(requests, experts):
    """
    Runs the matching function for each client request.
    Requires: requests (ClientsCollection), the collection of clients
    Requires: experts (ExpertsCollection), the collection of experts
    Ensures: tuple of (schedule, updatedExperts)
             schedule (Schedule) is the collection of matches for
              the schedule file.
             updatedExperts (ExpertsCollection) is the updated list of
              experts.
    """

    updatedExperts = ExpertsCollection(experts.getExpertsList())
    scheduleOutput = Schedule()

    for client in requests.items():
        matchResults = matchClient(client, updatedExperts)
        scheduleOutput.addToSchedule(matchResults[0])
        updatedExperts = matchResults[1]


def matchClient(client, experts):
    """
    Matches client with one expert from the
    Requires: client is Client
    Requires: experts is ExpertsCollection
    """

    # Collection that is going to be used in the match process:
    expertsCol = ExpertsCollection(experts.getExpertsList())

    # Collection that is going to be updated with new data:
    updatedExperts = ExpertsCollection(experts.getExpertsList())

    for i in expertsCol.items():
        i.addTravelTime()  # add the travel time to all in expertsCol

    # update the experts collection with only the suitable experts
    expertsCol.setCriteria(client.getMin_rating(),
                           client.getMax_hourly_charge(),
                           client.getZone())

    if expertsCol.count() == 0:  # if there are no compatible experts
        matchClientExpert = Match(False, client)  # return denied
        return (matchClientExpert, updatedExperts)
    else:
        # Temporary variable bestExpert using bestExpert() method
        bestExpert = expertsCol.bestExpert()

        # create match object with client and expert:
        matchClientExpert = Match(True, client, bestExpert)

        # check the time in which both are available and
        # set matchTime var to that time
        if client.getTime() < bestExpert.getTime():
            matchTime = bestExpert.getTime()
        else:
            matchTime = client.getTime()

        # Set time matchClientExpert time to matchTime
        matchClientExpert.setTime(matchTime)

        # amountEarned = INSERIR AQUI PREÇO DO SERVIÇO
        # endTime = INSERIR AQUI TEMPO DE CONCLUSÃO DO SERVIÇO

        # Updates the expert in the collection
        updatedExperts.updateMatchedExpert(bestExpert.getName(), endTime, amountEarned)

        # Returns the match and the updated list of experts
        return matchClientExpert, updatedExperts









