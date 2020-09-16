#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler

from datetime import datetime
import calendar

dr = DataReader('data\\data.csv')
dh = DataHandler()

allSessions = dr.sessions

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
            print(f'{calendar.month_name[month]}:')
            print(f'Number of sessions:{len(sessions)}')
            print('Total reps:{}')
            print('Total sets:{}')
            print('Average reps per session:{}')
            print('Average sets per session:{}')
            print()