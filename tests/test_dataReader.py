#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler

import pandas
from datetime import datetime

def test_dataReaderInit():
    dr = DataReader('tests\\test_data.csv')
    assert dr != None

def test_dataReaderContent():
    dr = DataReader('tests\\test_data.csv')
    expected = pandas.DataFrame({'Date': ['2019-04-06'], 'Exercise': ['Snatch'], 'Reps': [1], 'Weight': [68]})
    actual = dr.getData()

    assert actual['Date'][0] == expected['Date'][0]