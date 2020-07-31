#! python3

from dataReader import dataReader
from dataHandler import dataHandler

dr = dataReader('lifting_data.csv')

dh = dataHandler()

print(dh.getExerciseMax(dr.getData(), 'Snatch', 1))