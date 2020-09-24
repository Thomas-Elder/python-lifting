#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler

from datetime import datetime
import calendar

dr = DataReader('data\\data.csv')
dh = DataHandler()

allSessions = dr.sessions

exercise = 'Squat'