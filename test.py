from timeit import default_timer as timer
from datetime import datetime

from data.dataReader import DataReader
from data.dataReader_Sort import DataReader_Sort
from data.dataHandler import DataHandler

start = timer()
#dr = DataReader('data\\data.csv')
end = timer()

print(f'Data reader init exection time: {round(end-start, 2)} seconds') #  5.98 seconds

start = timer()
dr = DataReader_Sort('data\\data.csv')
end = timer()

print(f'Data reader sort init exection time: {round(end-start, 2)} seconds') #  5.98 seconds

print()
print(f'Current list of sessions: {len(dr.sessions)}')
print(f'Session exercises:')
for exercise in dr.sessions[datetime(2020, 10, 6, 0, 0)].exercises:
    print(f'Exercise name: {exercise.name}')
