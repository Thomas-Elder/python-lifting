#! python3

from data.dataReader import dataReader
from data.dataHandler import dataHandler

def test_dataReaderInit():
    dr = dataReader('data\\lifting_data.csv')
    assert dr != None