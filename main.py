#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler
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

print('len(competitionDates): {}'.format(len(competitionDates)))
print('Lifts on competition dates: \n{}'.format(dh.getExercises(dr.getData(fromDate=competitionDates[0], toDate=competitionDates[0]))))