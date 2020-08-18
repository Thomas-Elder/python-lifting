#! python3

# Imports
from data.dataHandler import DataHandler

import pandas
import numpy
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Test_DataHandler():

    def setup_method(self):
        logging.info('Setting up before test... ')
        self.dh = DataHandler()
        self.testDataFrame = pandas.DataFrame({
            'Date': [pandas.to_datetime('2020-04-01'), 
                    pandas.to_datetime('2020-04-20'), 
                    pandas.to_datetime('2020-05-01'), 
                    pandas.to_datetime('2020-05-30'), 
                    pandas.to_datetime('2020-06-01'), 
                    pandas.to_datetime('2020-06-01'), 
                    pandas.to_datetime('2020-06-01'), 
                    pandas.to_datetime('2020-06-01'), 
                    pandas.to_datetime('2020-07-01'), 
                    pandas.to_datetime('2020-07-30')], 
            'Exercise': ['Snatch', 'Snatch', 'Snatch', 'Snatch','Snatch', 'Snatch', 'Snatch', 'Snatch', 'Snatch', 'Snatch'], 
            'Reps': [1, 1, 3, 3, 2, 1, 1, 1, 2, 2], 
            'Weight': [10, 10, 10, 10, 20, 30, 40, 50, 30, 20],
            'Attempt': [0, 1, 0, 0, 0, 1, 2, 3, 0, 0]})

    def teardown_method(self):
        logging.info('Tearing down after test... ')
        self.dh = None

    def test_getExercises(self):
        exercises = ['Snatch']
        assert self.dh.getExercises(self.testDataFrame) == exercises

    def test_getSets(self):
        expected_Sets = pandas.DataFrame({
            'Date': [pandas.to_datetime('2020-06-01'), 
                    pandas.to_datetime('2020-06-01'), 
                    pandas.to_datetime('2020-06-01'), 
                    pandas.to_datetime('2020-06-01')
                    ], 
            'Exercise': ['Snatch', 'Snatch', 'Snatch', 'Snatch'], 
            'Reps': [2, 1, 1, 1], 
            'Weight': [20, 30, 40, 50],
            'Attempt': [0, 1, 2, 3]})
        date = pandas.to_datetime('2020-06-01')
        
        result = self.dh.getSets(self.testDataFrame, date, date)

        logging.debug('result:{}'.format(result))
        logging.debug('expected_Sets:{}'.format(expected_Sets))

        # The dataframe comes back with the index from it's position in 
        # the dataframe passed, so the expected sets have index 0,1,2,3,
        # and the result has index 4,5,6,7.
        # This line just resets the index of the result.
        result.reset_index(drop=True, inplace=True)

        assert numpy.all(result == expected_Sets)

    def test_getReps(self):
        testReps = '1X1'
        result = self.dh.getReps(testReps)

        assert result == {'total':3, 'successful': 2, 'failed':1}

    def test_getExerciseMaxAverage(self):
        exercise, rep, weight = 'Snatch', 3, 10.0
        assert self.dh.getExerciseMaxAverage(self.testDataFrame, exercise, rep) == weight

    def test_getExerciseMax(self):
        exercise, rep, weight = 'Snatch', 1, 50.0
        assert self.dh.getExerciseMax(self.testDataFrame, exercise, rep) == weight

    def test_getExerciseMaxes(self):
        exercise, rep = 'Snatch', 3
        expected_exerciseMaxes = [{'Date':pandas.to_datetime('2020-05-01'), 'Weight':10},
                                {'Date':pandas.to_datetime('2020-05-30'), 'Weight':10}]

        result = self.dh.getExerciseMaxes(self.testDataFrame, exercise, rep)
        
        assert numpy.all(result == expected_exerciseMaxes)

    def test_getCompetitionDates(self):
        expected_competitionDates = [pandas.to_datetime('2020-04-20'), pandas.to_datetime('2020-06-01')]
        result = self.dh.getCompetitionDates(self.testDataFrame)
        assert numpy.all(result == expected_competitionDates)

        # loggedy doggedy doo
        logging.debug('pandas.to_datetime(2020-04-20): {}'.format(pandas.to_datetime('2020-04-20')))
        logging.debug('type(pandas.to_datetime(\'2020-04-20\')): {}'.format(type(pandas.to_datetime('2020-04-20'))))
        logging.debug('result: {}'.format(result))
        logging.debug('type(result[0]): {}'.format(type(result[0])))
        logging.debug('expected_competitionDates: {}'.format(expected_competitionDates))
        logging.debug('type(expected_competitionDates[0]): {}'.format(type(expected_competitionDates[0])))

        #assert numpy.all(result == expected_competitionDates)

    def test_getPeriodDates(self):
        competitionDates = [pandas.to_datetime('2020-04-20'), pandas.to_datetime('2020-06-01')]
        expected_periodDates = [(pandas.to_datetime('2020-04-01'), pandas.to_datetime('2020-04-19')), 
                                (pandas.to_datetime('2020-04-21'), pandas.to_datetime('2020-05-31')), 
                                (pandas.to_datetime('2020-06-02'), pandas.to_datetime('2020-07-30'))]
        
        result = self.dh.getPeriodDates(self.testDataFrame, competitionDates)

        assert numpy.all(result == expected_periodDates)