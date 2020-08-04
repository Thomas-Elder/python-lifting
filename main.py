#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler
import pandas

dr = DataReader('data\\data.csv')

dh = DataHandler()

print(dh.getExerciseMax(dr.getData(), 'Snatch', 1))
print(dh.getExerciseMax(dr.getData(), 'Clean and Jerk', 1))

testDataFrame = pandas.DataFrame({
            'Date': ['2020-05-01', '2020-06-01', '2020-06-01', '2020-06-01', '2020-06-01', '2020-07-01', '2020-07-01'], 
            'Exercise': ['Snatch', 'Snatch', 'Snatch', 'Snatch', 'Snatch', 'Snatch', 'Snatch'], 
            'Reps': [1, 2, 3, 4, 5, 4, 3], 
            'Weight': [10, 20, 30, 40, 50, 30, 20],
            'Attempt': ['','',1,2,3,'','']})

expected_competitionDates = ['2020-06-01']
result = dh.getCompetitionDates(testDataFrame)
assert result == expected_competitionDates