#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler

dr = DataReader('data\\data.csv')

dh = DataHandler()

print(dh.getExerciseMax(dr.getData(), 'Snatch', 1))