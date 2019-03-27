"""
Eu criei este módulo apenas para testar
classes e fazer debug. Não serve para nada.
-Gil
"""
from dateTime import dateTime
from Expert import Expert
from ExpertsCollection import ExpertsCollection

'''
expert1 = Expert('Toze', 'lisbon', ('s1', 's2'), 4, 2, 'N/A', 10)
col1 = ExpertsCollection()

col1.addExpert(expert1)

col1.setCriteria(4, 4, 'lisbon')

# print(expert1)

# print experts in the collection:
for i in col1.items:
    print(i)

print(col1.outputData())
'''


time1 = dateTime(2019, 1, 2, 9, 1)
time2 = dateTime(2019, 1, 1, 8, 2)
time3 = dateTime(2019, 1, 1, 10, 0)

exp1 = Expert('Exp1', 'lisbon', ('s1', 's2'), 4, 2, time1, 10)
exp2 = Expert('Exp2', 'lisbon', ('s1', 's2'), 4, 2, time2, 10)
exp3 = Expert('Exp3', 'lisbon', ('s1', 's2'), 4, 2, time3, 10)


col1 = ExpertsCollection([exp1, exp2, exp3])

print(col1)

col1.sortExpertsByTime()

print(col1)
