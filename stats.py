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

sessions = []

for year in range(startYear, endYear + 1):

    yearSessions = [session for session in allSessions if session.date.year == year]

    months = []
    for session in yearSessions:
        if session.date.month not in months:
            months.append(session.date.month)

    monthlySessions = []
    for month in months:
        monthlySessions.append({month: [session for session in yearSessions if session.date.month == month]})

    sessions.append({year: monthlySessions})

for s in sessions:
    print(s)