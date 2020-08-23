#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler

from datetime import datetime
import pandas

dr = DataReader('data\\data.csv')
dh = DataHandler()

print()
print('Lets get real data now... ')

allData = dr.sessions
competitionDates = dh.getCompetitionDates(allData)
trainingPeriods = dh.getPeriodDates(competitionDates)

print()
print('Dates of competition:{}'.format(competitionDates))
print('Training periods: {}'.format(trainingPeriods))

print()
for date in competitionDates:
    session = dh.getSessions(allData, fromDate=date, toDate=date, competition=True)

    print('Lifts on competition dated: {}'.format(session.date))
    for e in session.exercises:

        print('{} lifts:'.format(e.name))
        for s in e.sets:
            print('successfulRepetitions: {}, failedRepetitions: {}, weight: {}'.format(s.successfulRepetitions, s.failedRepetitions, s.weight))
        
        print()

print()
print('Training period data')
for period in trainingPeriods:

    periodData = dh.getSessions(allData, period[0], period[1])

    print()
    print('For training period {}:{}'.format(datetime.strftime(period[0], '%Y-%m-%d'), datetime.strftime(period[1], '%Y-%m-%d')))

    for exercise in dh.getExercises(periodData):

        exerciseMaxAverage = dh.getExerciseMaxAverage(periodData, exercise, 3)

        if exerciseMaxAverage != 0:
            print('Average max weight for {} 3s was: {}'.format(exercise, exerciseMaxAverage))