#! python3

# Imports
from data.dataReader import DataReader
from data.dataHandler import DataHandler

from datetime import datetime
import pandas
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Test_DataReader():

    def setup_method(self):
        logging.info('Setting up before test... ')
        self.dr = DataReader('tests\\test_data.csv')
    
    def teardown_method(self):
        logging.info('Tearing down after test... ')
        self.dr = None

    def test_dataReaderInit(self):
        assert self.dr != None

    def test_dataReaderContent(self):
        expected = pandas.DataFrame({'Date': ['2019-04-06'], 'Exercise': ['Snatch'], 'Reps': [1], 'Weight': [68]})
        actual = self.dr.getData()

        assert actual['Date'][0] == expected['Date'][0]