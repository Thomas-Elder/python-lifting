#! python3

from data.dataReader import dataReader
from data.dataHandler import dataHandler

dr = dataReader('data\\data.csv')

dh = dataHandler()

print(dh.getExerciseMax(dr.getData(), 'Snatch', 1))