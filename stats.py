#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler

from datetime import datetime
import calendar

dr = DataReader('data\\data.csv')
dh = DataHandler()

allSessions = dr.sessions

def monthlyStats(allSessions):

    monthlyStatsList = []

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

    for year in range(startYear, endYear + 1):

        print(f'{year}')
        for month in range(1, 13):       

            sessions = dh.getSessions(allSessions, datetime(year, month, 1), datetime(year, month, calendar.monthrange(year, month)[1]))
            if len(sessions) != 0:

                numberOfSessions = len(sessions)
                reps = 0
                sets = 0
                for session in sessions:
                    for exercise in session.exercises:
                        sets += len(exercise.sets)
                        for s in exercise.sets:
                            reps += s.totalRepetitions

                monthlyStatsList.append({'year': year, 
                                         'month': calendar.month_name[month],
                                         'numberOfSessions': numberOfSessions,
                                         'numberOfReps': reps,
                                         'numberOfSets': sets,
                                         'averageReps': round(reps/numberOfSessions,2),
                                         'averageSets': round(sets/numberOfSessions,2)})

    return monthlyStatsList

stats = monthlyStats(allSessions)

for stat in stats:
    year = stat['year']
    print(f'{stat["year"]}/{stat["month"]}:')
    print(f'Number of sessions:{stat["numberOfSessions"]}')
    print(f'Total reps:{stat["numberOfReps"]}')
    print(f'Total sets:{stat["numberOfSets"]}')
    print(f'Average reps per session:{stat["averageReps"]}')
    print(f'Average sets per session:{stat["averageSets"]}')
    print()