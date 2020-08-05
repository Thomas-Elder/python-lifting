#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler

from datetime import datetime
import pandas

dr = DataReader('data\\data.csv')

dh = DataHandler()

print()
print('Lets get real data now... ')

allData = dr.getData()
competitionDates = dh.getCompetitionDates(allData)
trainingPeriods = dh.getPeriodDates(allData, competitionDates)

print()
print('Dates of competition:{}'.format(competitionDates))
print('Training periods: {}'.format(trainingPeriods))

for i in range(len(competitionDates)):
    print()
    print('Lifts on competition dates: \n{}'.format(dh.getSets(dr.getData(), fromDate=competitionDates[i], toDate=competitionDates[i])))

print()
print('Training period data')
for i in range(len(trainingPeriods)):

    periodData = dr.getData(trainingPeriods[i][0], trainingPeriods[i][1])

    print()
    print('For training period {}:{}'.format(datetime.strftime(trainingPeriods[i][0], '%Y-%m-%d'), datetime.strftime(trainingPeriods[i][1], '%Y-%m-%d')))

    for exercise in dh.getExercises(periodData):

        exerciseMaxAverage = dh.getExerciseMaxAverage(periodData, exercise, 3)

        if exerciseMaxAverage != 0:
            print('Average max weight for {} 3s was: {}'.format(exercise, exerciseMaxAverage))

print()
print('The average max sets of 3 for each exercise, for each training period:{}'.format(exercise))  

for exercise in dh.getExercises(allData):

    for i in range(len(trainingPeriods)):
        periodData = dr.getData(trainingPeriods[i][0], trainingPeriods[i][1])
        exerciseMaxAverage = dh.getExerciseMaxAverage(periodData, exercise, 3)

        if exerciseMaxAverage != 0:
            print('For training period {}:{}'.format(datetime.strftime(trainingPeriods[i][0], '%Y-%m-%d'), datetime.strftime(trainingPeriods[i][1], '%Y-%m-%d')))
            print('Average max weight for {} 3s was: {}'.format(exercise, exerciseMaxAverage))