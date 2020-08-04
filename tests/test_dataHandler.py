#! python3

# Imports
from data.dataHandler import DataHandler

import pandas
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Test_DataHandler():

    def setup_method(self):
        logging.info('Setting up before test... ')
        self.dh = DataHandler()
        self.testDataFrame = pandas.DataFrame({
            'Date': ['2020-05-01', '2020-05-30','2020-06-01', '2020-06-01', '2020-06-01', '2020-06-01', '2020-07-01', '2020-07-30'], 
            'Exercise': ['Snatch', 'Snatch','Snatch', 'Snatch', 'Snatch', 'Snatch', 'Snatch', 'Snatch'], 
            'Reps': [3, 3, 2, 1, 1, 1, 2, 2], 
            'Weight': [10, 10, 20, 30, 40, 50, 30, 20],
            'Attempt': ['','','',1,2,3,'','']})
    
    def teardown_method(self):
        logging.info('Tearing down after test... ')
        self.dh = None

    def test_getExercises(self):
        exercises = ['Snatch']
        assert self.dh.getExercises(self.testDataFrame) == exercises

    def test_getExerciseMaxAverage(self):
        exercise, rep, weight = 'Snatch', 3, 10.0
        assert self.dh.getExerciseMaxAverage(self.testDataFrame, exercise, rep) == weight

    def test_getExerciseMax(self):
        exercise, rep, weight = 'Snatch', 1, 50.0
        assert self.dh.getExerciseMax(self.testDataFrame, exercise, rep) == weight

    def test_getExerciseMaxes(self):
        exercise, rep, weight = 'Snatch', 3, 10.0
        assert self.dh.getExerciseMaxAverage(self.testDataFrame, exercise, rep) == weight

    def test_getCompetitionDates(self):
        expected_competitionDates = ['2020-06-01']
        result = self.dh.getCompetitionDates(self.testDataFrame)
        assert result == expected_competitionDates
        