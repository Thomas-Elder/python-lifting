#! python3

# Imports
from data.dataReader import DataReader
from data.dataHandler import DataHandler
from data.models.exercise import Exercise
from data.models.set import Set
from data.models.session import Session

from datetime import datetime
import pandas
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Test_DataReader():

    def setup_method(self):
        logging.info('Setting up before test... ')
        self.dr = DataReader('./tests/test_data.csv')
    
    def teardown_method(self):
        logging.info('Tearing down after test... ')
        self.dr = None

    def test_dataReaderInit(self):
        assert self.dr != None

    def test_dataReaderContent(self):
        expected = pandas.DataFrame({'Date': pandas.to_datetime('2020-07-18'), 'Exercise': ['Snatch'], 'Reps': [3], 'Weight': [30], 'Attempt': 0})
        actual = self.dr.getData()

        assert actual['Date'][0] == expected['Date'][0]

    def test_translateData(self):
        data = pandas.DataFrame({'Date': pandas.to_datetime('2020-07-18'), 'Exercise': ['Snatch'], 'Reps': [3], 'Weight': [30], 'Attempt': 0})
        data = self.dr.getData()
        
        expectedDate = pandas.to_datetime('2020-07-18')
        expectedExerciseName = 'Snatch'
        expectedWeight = 30

        self.dr.translateData(data)
        actual = self.dr.sessions

        assert actual[0].date == expectedDate
        assert actual[0].exercises[0].name == expectedExerciseName
        assert actual[0].exercises[0].sets[0].weight == expectedWeight