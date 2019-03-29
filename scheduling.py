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

def update(requests, experts, scheduleTime):
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

    newExperts = ExpertsCollection(experts.getExpertsList())
    scheduleOutput = Schedule()

    for client in requests.items():
        matchResults = matchClient(client, newExperts, scheduleTime)
        scheduleOutput.addToSchedule(matchResults[0])
        newExperts = matchResults[1]


    return scheduleOutput, newExperts


def matchClient(client, experts, scheduleTime):
    """
    Matches client with one expert from the
    Requires: client is Client
    Requires: experts is ExpertsCollection
    """

    # Collection that is going to be used in the match process:
    expertsCol = ExpertsCollection(experts.getExpertsList())
    updatedExperts = deepcopy(expertsCol)

    # add the travel time to all experts in expertsCol
    expertsCol.addTravelTime()


    # update the experts collection with only the suitable experts
    expertsCol.setCriteria(client.getMin_rating(),
                           client.getMax_hourly_charge(),
                           client.getZone(),
                           client.getRequired_expertise())


    if expertsCol.count() == 0:  # if there are no compatible experts
        matchClientExpert = Match(False, client, 'N/A', scheduleTime)  # return denied
        return matchClientExpert, updatedExperts
    else:  # if 'if' clause is False, there is >= 1 compatible expert
        # Temporary variable bestExpert using bestExpert() method
        bestExpert = expertsCol.bestExpert()

        # create match object with client and expert:
        matchClientExpert = Match(True, client, bestExpert)

        # check the time in which both are available and
        # set matchTime var to that time
        if client.getDateTime() < bestExpert.getDateTime():
            matchTime = bestExpert.getDateTime()

        else:
            matchTime = client.getDateTime()

        # Set time matchClientExpert time to matchTime
        matchClientExpert.setTime(matchTime)

        # Amount earned by the expert
        amountEarned = bestExpert.getRate() * client.getDuration().floatHours()

        # timestamp in which the job ends
        endTime = deepcopy(matchTime)
        endTime.addTime(client.getDuration().getTotalMinutes())


        # Updates the expert in the collection
        updatedExperts.updateMatchedExpert(bestExpert.getName(), endTime, amountEarned)


        # Returns the match and the updated list of experts

        return matchClientExpert, updatedExperts









