#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler

from datetime import datetime
import pandas

dr = DataReader('data\\data.csv')
dh = DataHandler()

allData = dr.sessions

# now I want a list of sessions between day and month 3, month 3 and 6 etc
# So that's:
# 1Aug20 - 30Oct20
# 1Nov20 - 31Jan21
# 1Feb21 - 30Apr21
# 1May21 - 31Jul21

trainingPeriods = []
trainingPeriods.append({'dates': [pandas.to_datetime('2020-8-1'), pandas.to_datetime('2020-10-30')], 'sessions': dh.getSessions(allData, pandas.to_datetime('2020-8-1'), pandas.to_datetime('2020-10-30'), competition=False)})
trainingPeriods.append({'dates': [pandas.to_datetime('2020-11-1'), pandas.to_datetime('2021-1-31')], 'sessions': dh.getSessions(allData, pandas.to_datetime('2020-11-1'), pandas.to_datetime('2021-1-31'), competition=False)})
trainingPeriods.append({'dates': [pandas.to_datetime('2021-2-1'), pandas.to_datetime('2020-4-30')], 'sessions': dh.getSessions(allData, pandas.to_datetime('2021-2-1'), pandas.to_datetime('2021-4-30'), competition=False)})
trainingPeriods.append({'dates': [pandas.to_datetime('2021-5-1'), pandas.to_datetime('2020-7-31')], 'sessions': dh.getSessions(allData, pandas.to_datetime('2021-5-1'), pandas.to_datetime('2021-7-31'), competition=False)})

# Then I want average top sets for the following for each period.
# Snatch pulls for 3
# Clean pulls for 3
# Front squat for 3
# Back squat for 3
# Power snatch for 3
# Power clean for 3
# Snatch balance for 3
keyExercises = ['Snatch Pull', 'Clean Pull', 'Front Squat', 'Back Squat', 'Power Snatch', 'Power Clean', 'Snatch Balance']

# Ok so let's run this for those exercises from the start of the year.
print()
print('Starting point... ')
for exercise in keyExercises:
    fromDate = pandas.to_datetime('2020-1-1')
    toDate = pandas.to_datetime('2020-7-30')

    print('{} : {}'.format(exercise, dh.getExerciseMaxAverage(dh.getSessions(allData, fromDate, toDate) , exercise, 3)))

# And then for all the 3 month training periods we've set for the year.
for period in trainingPeriods:
    print()
    print('For training period: {} - {}'.format(datetime.strftime(period['dates'][0], '%Y-%m-%d'), datetime.strftime(period['dates'][1], '%Y-%m-%d')))
    print('The average top set weight for 3s:')
    for exercise in keyExercises:
        print('{} : {}'.format(exercise, dh.getExerciseMaxAverage(dh.getSessions(allData, period['dates'][0], period['dates'][1]) , exercise, 3)))


# Ok then here are the weights we want to lift at the end of each period:
# Snatch Pull (3 reps)	    90	96	101	107	113
# Clean Pull (3 reps)	    106	112	118	124	130
# Front Squat (3 reps)	    86	91	96	101	106
# Back Squat (3 reps)	    93	98	104	109	114
# Power Snatch (3 reps)	    57	61	64	68	71
# Power Clean (3 reps)	    68	72	76	80	83
# Snatch Balance (3 reps)	71	75	80	84	89

# So goals: 
targets = [{'exercise': 'Snatch Pull', 'weights': [96, 101, 107, 113]},
            {'exercise': 'Clean Pull', 'weights': [112, 118, 124, 130]},
            {'exercise': 'Front Squat', 'weights': [91, 96, 101, 106]},
            {'exercise': 'Back Squat', 'weights': [98, 104, 109, 114]},
            {'exercise': 'Power Snatch', 'weights': [61, 64, 68, 71]},
            {'exercise': 'Power Clean', 'weights': [72, 76, 80, 83]},
            {'exercise': 'Snatch Balance', 'weights': [75, 80, 84, 89]}]

