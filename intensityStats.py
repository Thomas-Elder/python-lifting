#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler

from datetime import datetime
import calendar

dr = DataReader('data\\data.csv')
dh = DataHandler()

allSessions = dr.sessions

exercise = 'Back Squat'


def monthlyIntensityStats(allSessions):

    #monthlyStatsList = []

    startYear = datetime.today().year
    endYear = datetime.today().year
    years = []

    for session in allSessions:
        if session.date.year not in years:
            years.append(session.date.year)

        if session.date.year > endYear:
            endYear = session.date.year

        if session.date.year < startYear:
            startYear = session.date.year

    competitionLifts = dh.getCompetitionLifts(dh.getSessions(allSessions, datetime(2000, 1, 1), datetime(2030, 12, 31), competition=True))

    for year in range(startYear, endYear + 1):

        print(f'{year}')
        for month in range(1, 13):       

            sessions = dh.getSessionsForExercise(allSessions, datetime(year, month, 1), datetime(year, month, calendar.monthrange(year, month)[1]), exercise)
            
            if len(sessions) != 0:
                
                monthlyTotalWeight = 0
                monthlyTotalIntensity = 0

                for session in sessions:

                    ex = [e for e in session.exercises if e.name == exercise]

                    print()
                    for e in ex:
                        print(session.date)
                        print(f'Exercise: {e.name}')
                        print(f'Weight: {e.topSet().weight}')
                        print(f'Intensity: {e.topSetIntensity(competitionLifts)}%')

                        monthlyTotalWeight += e.topSet().weight
                        monthlyTotalIntensity += e.topSetIntensity(competitionLifts)

                monthlyAverageWeight = round(monthlyTotalWeight / len(sessions), 2)
                monthlyAverageIntensity = round(monthlyTotalIntensity / len(sessions), 2)

                print()
                print(f'Monthly average weight: {monthlyAverageWeight}')
                print(f'Monthly average intensity: {monthlyAverageIntensity}')

monthlyIntensityStats(allSessions)