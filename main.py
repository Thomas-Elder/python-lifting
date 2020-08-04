#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler
import pandas

dr = DataReader('data\\data.csv')

dh = DataHandler()

print(dh.getExerciseMax(dr.getData(), 'Snatch', 1))
print(dh.getExerciseMax(dr.getData(), 'Clean and Jerk', 1))

testDataFrame = pandas.DataFrame({
            'Date': ['2020-05-01', '2020-05-30','2020-06-01', '2020-06-01', '2020-06-01', '2020-06-01', '2020-07-01', '2020-07-30'], 
            'Exercise': ['Snatch', 'Snatch','Snatch', 'Snatch', 'Snatch', 'Snatch', 'Snatch', 'Snatch'], 
            'Reps': [3, 3, 2, 1, 1, 1, 2, 2], 
            'Weight': [10, 10, 20, 30, 40, 50, 30, 20],
            'Attempt': ['','','',1,2,3,'','']})

exercise = 'Snatch'
reps = 2

print(testDataFrame.loc[testDataFrame['Exercise'] == 'Snatch'])
print(testDataFrame.loc[(testDataFrame['Exercise'] == exercise) & (testDataFrame['Reps'] == reps)])
print(testDataFrame.loc[(testDataFrame['Exercise'] == exercise) & (testDataFrame['Reps'] == reps)].max())
print(testDataFrame.loc[(testDataFrame['Exercise'] == exercise) & (testDataFrame['Reps'] == reps)].max()['Weight'])