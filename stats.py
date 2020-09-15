#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler

from datetime import datetime

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

periods = {2019: [], 2020: []}

for year in range(startYear, endYear + 1):

    for session in allSessions:
        if session.date.year == year and session.date.month not in periods[year]:
            periods[year].append(session.date.month)

print(periods)