#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler

from datetime import datetime

dr = DataReader('data\\data.csv')
dh = DataHandler()

allSessions = dr.sessions

monthsA = []
for session in allSessions:
    if session.date.month not in monthsA:
        monthsA.append(session.date.month)

months = [session.date.month for session in allSessions if session.date.month not in months]

print(monthsA)
print(months)