#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler

from datetime import datetime

dr = DataReader('data\\data.csv')
dh = DataHandler()

allData = dr.sessions

# now I want a list of sessions between day and month 3, month 3 and 6 etc
# So that's:
# 1Aug20 - 30Oct20
# 1Nov20 - 31Jan21
# 1Feb21 - 30Apr21
# 1May21 - 31Jul21

# Then I want average top sets for the following for each period.
# Snatch pulls for 3
# Clean pulls for 3
# Front squat for 3
# Back squat for 3
# Power snatch for 3
# Power clean for 3
# Snatch balance for 1