#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler

from datetime import datetime

dr = DataReader('data\\data.csv')
dh = DataHandler()

allData = dr.sessions

# now I want a list of sessions between day and month 3, month 3 and 6 etc
# So that's:
# 1Aug20 - 30Oct20
# 1Nov20 - 31Jan21
# 1Feb21 - 30Apr21
# 1May21 - 31Jul21

# Then I want average top sets for the following for each period.
# Snatch pulls for 3
# Clean pulls for 3
# Front squat for 3
# Back squat for 3
# Power snatch for 3
# Power clean for 3
# Snatch balance for 3
keyExercises = [{'exercise': 'Snatch Pull'}, 
                {'exercise': 'Clean Pull'}, 
                {'exercise': 'Front Squat'}, 
                {'exercise': 'Back Squat'}, 
                {'exercise': 'Power Snatch'}, 
                {'exercise': 'Power Clean'}, 
                {'exercise': 'Snatch Balance'}
                ]

# Then here are the weights we want to lift at the end of each period:
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

# Ok I think I want to tie all this together temporarily... 
# What data do I want to display: 
# Training Period x to y
# Exercise: Top Set Average: Target Average:
#
# So I need 4 training period objects, with a list of exercises. Each exercise needs to have an actual and goal weight.

trainingPeriods = []
trainingPeriods.append({'dates': [datetime.strptime('2020-8-1', '%Y-%m-%d'), datetime.strptime('2020-10-30', '%Y-%m-%d')], 
                        'exercises': [{'exercise': 'Snatch Pull', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-8-1', '%Y-%m-%d'), datetime.strptime('2020-10-30', '%Y-%m-%d')) , 'Snatch Pull', 3), 'target': 96}, 
                                     {'exercise': 'Clean Pull', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-8-1', '%Y-%m-%d'), datetime.strptime('2020-10-30', '%Y-%m-%d')) , 'Clean Pull', 3), 'target': 112}, 
                                     {'exercise': 'Front Squat', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-8-1', '%Y-%m-%d'), datetime.strptime('2020-10-30', '%Y-%m-%d')) , 'Front Squat', 3), 'target': 91}, 
                                     {'exercise': 'Back Squat', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-8-1', '%Y-%m-%d'), datetime.strptime('2020-10-30', '%Y-%m-%d')) , 'Back Squat', 3), 'target': 98}, 
                                     {'exercise': 'Power Snatch', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-8-1', '%Y-%m-%d'), datetime.strptime('2020-10-30', '%Y-%m-%d')) , 'Power Snatch', 3), 'target': 61}, 
                                     {'exercise': 'Power Clean', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-8-1', '%Y-%m-%d'), datetime.strptime('2020-10-30', '%Y-%m-%d')) , 'Power Clean', 3), 'target': 72}, 
                                     {'exercise': 'Snatch Balance', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-8-1', '%Y-%m-%d'), datetime.strptime('2020-10-30', '%Y-%m-%d')) , 'Snatch Balance', 3), 'target': 75}
                                    ]
                       })

trainingPeriods.append({'dates': [datetime.strptime('2020-11-1', '%Y-%m-%d'), datetime.strptime('2021-1-31', '%Y-%m-%d')], 
                        'exercises': [{'exercise': 'Snatch Pull', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-11-1', '%Y-%m-%d'), datetime.strptime('2021-1-31', '%Y-%m-%d')) , 'Snatch Pull', 3), 'target': 101}, 
                                     {'exercise': 'Clean Pull', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-11-1', '%Y-%m-%d'), datetime.strptime('2021-1-31', '%Y-%m-%d')) , 'Clean Pull', 3), 'target': 118}, 
                                     {'exercise': 'Front Squat', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-11-1', '%Y-%m-%d'), datetime.strptime('2021-1-31', '%Y-%m-%d')) , 'Front Squat', 3), 'target': 96}, 
                                     {'exercise': 'Back Squat', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-11-1', '%Y-%m-%d'), datetime.strptime('2021-1-31', '%Y-%m-%d')) , 'Back Squat', 3), 'target': 104}, 
                                     {'exercise': 'Power Snatch', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-11-1', '%Y-%m-%d'), datetime.strptime('2021-1-31', '%Y-%m-%d')) , 'Power Snatch', 3), 'target': 64}, 
                                     {'exercise': 'Power Clean', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-11-1', '%Y-%m-%d'), datetime.strptime('2021-1-31', '%Y-%m-%d')) , 'Power Clean', 3), 'target': 76}, 
                                     {'exercise': 'Snatch Balance', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-11-1', '%Y-%m-%d'), datetime.strptime('2021-1-31', '%Y-%m-%d')) , 'Snatch Balance', 3), 'target': 80}
                                    ]
                       })

trainingPeriods.append({'dates': [datetime.strptime('2021-2-1', '%Y-%m-%d'), datetime.strptime('2021-4-30', '%Y-%m-%d')], 
                        'exercises': [{'exercise': 'Snatch Pull', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2021-2-1', '%Y-%m-%d'), datetime.strptime('2021-4-30', '%Y-%m-%d')) , 'Snatch Pull', 3), 'target': 107}, 
                                     {'exercise': 'Clean Pull', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2021-2-1', '%Y-%m-%d'), datetime.strptime('2021-4-30', '%Y-%m-%d')) , 'Clean Pull', 3), 'target': 124}, 
                                     {'exercise': 'Front Squat', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2021-2-1', '%Y-%m-%d'), datetime.strptime('2021-4-30', '%Y-%m-%d')) , 'Front Squat', 3), 'target': 101}, 
                                     {'exercise': 'Back Squat', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2021-2-1', '%Y-%m-%d'), datetime.strptime('2021-4-30', '%Y-%m-%d')) , 'Back Squat', 3), 'target': 109}, 
                                     {'exercise': 'Power Snatch', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2021-2-1', '%Y-%m-%d'), datetime.strptime('2021-4-30', '%Y-%m-%d')) , 'Power Snatch', 3), 'target': 68}, 
                                     {'exercise': 'Power Clean', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2021-2-1', '%Y-%m-%d'), datetime.strptime('2021-4-30', '%Y-%m-%d')) , 'Power Clean', 3), 'target': 80}, 
                                     {'exercise': 'Snatch Balance', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2021-2-1', '%Y-%m-%d'), datetime.strptime('2021-4-30', '%Y-%m-%d')) , 'Snatch Balance', 3), 'target': 84}
                                    ]
                       })

trainingPeriods.append({'dates': [datetime.strptime('2021-5-1', '%Y-%m-%d'), datetime.strptime('2021-7-31', '%Y-%m-%d')], 
                        'exercises': [{'exercise': 'Snatch Pull', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2021-5-1', '%Y-%m-%d'), datetime.strptime('2021-7-31', '%Y-%m-%d')) , 'Snatch Pull', 3), 'target': 113}, 
                                     {'exercise': 'Clean Pull', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2021-5-1', '%Y-%m-%d'), datetime.strptime('2021-7-31', '%Y-%m-%d')) , 'Clean Pull', 3), 'target': 130}, 
                                     {'exercise': 'Front Squat', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2021-5-1', '%Y-%m-%d'), datetime.strptime('2021-7-31', '%Y-%m-%d')) , 'Front Squat', 3), 'target': 106}, 
                                     {'exercise': 'Back Squat', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2021-5-1', '%Y-%m-%d'), datetime.strptime('2021-7-31', '%Y-%m-%d')) , 'Back Squat', 3), 'target': 114}, 
                                     {'exercise': 'Power Snatch', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2021-5-1', '%Y-%m-%d'), datetime.strptime('2021-7-31', '%Y-%m-%d')) , 'Power Snatch', 3), 'target': 71}, 
                                     {'exercise': 'Power Clean', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2021-5-1', '%Y-%m-%d'), datetime.strptime('2021-7-31', '%Y-%m-%d')) , 'Power Clean', 3), 'target': 83}, 
                                     {'exercise': 'Snatch Balance', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2021-5-1', '%Y-%m-%d'), datetime.strptime('2021-7-31', '%Y-%m-%d')) , 'Snatch Balance', 3), 'target': 89}
                                    ]
                       })


# First let's print the data for everything prior to 1Aug20.
startingPoint = {'dates': [datetime.strptime('2020-5-1', '%Y-%m-%d'), datetime.strptime('2020-7-31', '%Y-%m-%d')], 
                'exercises': [{'exercise': 'Snatch Pull', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-5-1', '%Y-%m-%d'), datetime.strptime('2020-7-31', '%Y-%m-%d')) , 'Snatch Pull', 3)}, 
                                {'exercise': 'Clean Pull', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-5-1', '%Y-%m-%d'), datetime.strptime('2020-7-31', '%Y-%m-%d')) , 'Clean Pull', 3)}, 
                                {'exercise': 'Front Squat', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-5-1', '%Y-%m-%d'), datetime.strptime('2020-7-31', '%Y-%m-%d')) , 'Front Squat', 3)}, 
                                {'exercise': 'Back Squat', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-5-1', '%Y-%m-%d'), datetime.strptime('2020-7-31', '%Y-%m-%d')) , 'Back Squat', 3)}, 
                                {'exercise': 'Power Snatch', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-5-1', '%Y-%m-%d'), datetime.strptime('2020-7-31', '%Y-%m-%d')) , 'Power Snatch', 3)}, 
                                {'exercise': 'Power Clean', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-5-1', '%Y-%m-%d'), datetime.strptime('2020-7-31', '%Y-%m-%d')) , 'Power Clean', 3)}, 
                                {'exercise': 'Snatch Balance', 'actual': dh.getExerciseMaxAverage(dh.getSessions(allData, datetime.strptime('2020-5-1', '%Y-%m-%d'), datetime.strptime('2020-7-31', '%Y-%m-%d')) , 'Snatch Balance', 3)}
                            ]
                }

print()
print('Printing the average maximum weight lifted in each session, for 3 reps for the target exercises.')
print('First initial averages:')
print()
print('For training period: {} - {}'.format(datetime.strftime(startingPoint['dates'][0], '%Y-%m-%d'), datetime.strftime(startingPoint['dates'][1], '%Y-%m-%d')))
print('{:15}{:>10}'.format('Exercise', 'Actual'))
for exercise in startingPoint['exercises']:
    print('{:15}{:10}'.format(exercise['exercise'], exercise['actual']))

print()
print('Now printing the actual and target averages for the training periods over the year.')
# Print all the training period data
for period in trainingPeriods:
    print()
    print('For training period: {} - {}'.format(datetime.strftime(period['dates'][0], '%Y-%m-%d'), datetime.strftime(period['dates'][1], '%Y-%m-%d')))
    print('{:15}{:>10}{:>10}'.format('Exercise', 'Actual', 'Target'))
    for exercise in period['exercises']:
        print('{:15}{:10}{:10}'.format(exercise['exercise'], exercise['actual'], exercise['target']))
