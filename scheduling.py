# 2018-2019 Programação 2 (LTI)
# Grupo 34
# 49269 Mário Gil Oliveira
# 46261 Margarida Rolo

from copy import deepcopy
from ExpertsCollection import ExpertsCollection
from Match import Match

def update():
    """
    Função obrigatória tendo em conta a especificação
    """
    pass


def matchclient(client, experts):
    """
    Matches client with one expert from the
    Requires: client is Client
    Requires: experts is ExpertsCollection
    """

    expertsCol = ExpertsCollection(experts.getExpertsList())
    updatedExperts = ExpertsCollection(experts.getExpertsList())

    '''
    for i in expertsCol.items():
        i.addTravelTime()
    '''

    # update the experts collection with only the suitable experts
    expertsCol.setCriteria(client.getMin_rating(),
                           client.getMax_hourly_charge(),
                           client.getZone())


    if expertsCol.count() == 0:
        matchClientExpert = Match(False, client)
    else:
        bestExpert = expertsCol.bestExpert()
        matchclientExpert = Match(True, client, bestExpert)




