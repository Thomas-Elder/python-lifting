#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler

from datetime import datetime

dr = DataReader('data\\data.csv')
dh = DataHandler()

allData = dr.sessions

# So for a set of exercises I want to get a success/fail rate for lifts. 
keyExercises = ['Snatch',
                'Clean and Jerk'
                ]

for exercise in keyExercises:
    print(f"Success rate for {exercise}: {dh.getSuccessRate(allData, exercise, 1)*100}%")