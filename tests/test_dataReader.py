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
        expected = pandas.DataFrame({'Date': datetime.strptime('2020-07-18', '%Y-%m-%d'), 'Exercise': ['Snatch'], 'Reps': [3], 'Weight': [30], 'Attempt': 0})
        sessions = self.dr.sessions

        assert sessions[0].date == expected['Date'][0]

    def test_translateData(self):

        data = self.dr.getData()
        
        expectedDate = datetime.strptime('2020-07-18', '%Y-%m-%d')
        expectedExerciseName = 'Snatch'
        expectedWeight = 30

        actual = self.dr.translateData(data, self.dr.translateRepetitions)

        assert actual[0].date == expectedDate
        assert actual[0].exercises[0].name == expectedExerciseName
        assert actual[0].exercises[0].sets[0].weight == expectedWeight
        assert actual[0].exercises[0].sets[0].totalRepetitions == 3
        assert len(actual[0].exercises[0].sets) == 13

    def test_translateRepetitions(self):

        testRepetitionString = '1X1X5XXX3'

        expected = (15, 10, 5)
        actual = self.dr.translateRepetitions(testRepetitionString)

        assert actual == expected

    def test_dataReaderSessions(self):
        
        assert self.dr.sessions[0].competition == True
        assert self.dr.sessions[1].competition == False
