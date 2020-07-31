#! python3

from data.dataReader import DataReader
from data.dataHandler import DataHandler

import pandas
from datetime import datetime

class Test_DataReader():

    def setup_method(self):
        self.dr = DataReader('tests\\test_data.csv')
    
    def teardown_method(self):
        self.dr = None

    def test_dataReaderInit(self):
        #dr = DataReader('tests\\test_data.csv')
        assert self.dr != None

    def test_dataReaderContent(self):
        #dr = DataReader('tests\\test_data.csv')
        expected = pandas.DataFrame({'Date': ['2019-04-06'], 'Exercise': ['Snatch'], 'Reps': [1], 'Weight': [68]})
        actual = self.dr.getData()

        assert actual['Date'][0] == expected['Date'][0]