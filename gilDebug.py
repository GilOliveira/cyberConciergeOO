"""
Eu criei este módulo apenas para testar
classes e fazer debug. Não serve para nada.
-Gil
"""
from DateTime import dateTime
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

from filesReading import *

print(str(readClients('2019y01m12clients09h00.txt')))