from timeit import default_timer as timer

from data.dataReader import DataReader
from data.dataHandler import DataHandler

start = timer()
dr = DataReader('data\\data.csv')
end = timer()

print(f'Data reader init exection time: {round(end-start, 2)} seconds') #  5.98 seconds