#! python3

# Imports
import pytest

from data.dataHandler import DataHandler
from data.models.session import Session
from data.models.exercise import Exercise
from data.models.set import Set

import pandas
import numpy
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def test_data():
    testSessions = []

    session = Session(pandas.to_datetime('2020-04-01'))

    exercises = []

    exercises.append(Exercise('Snatch'))
    exercises.append(Exercise('Clean and Jerk'))

    exercises[0].sets = [Set(3, 2, 1, 30), Set(1, 1, 0, 10), Set(3, 3, 0, 20), Set(3, 3, 0, 15)]
    exercises[1].sets = [Set(3, 2, 1, 50), Set(3, 3, 0, 20), Set(3, 3, 0, 30), Set(3, 3, 0, 45)]

    session.addExercise(exercises[0])
    session.addExercise(exercises[1])

    testSessions.append(session)

    return testSessions

class Test_DataHandler():

    def setup_method(self):
        logging.info('Setting up before test... ')
        self.dh = DataHandler()

    def teardown_method(self):
        logging.info('Tearing down after test... ')
        self.dh = None

    def test_getExercises(self, test_data):
        exercises = ['Snatch', 'Clean and Jerk']
        assert self.dh.getExercises(test_data) == exercises

    def test_getSets(self):

        assert 0

    def test_getReps(self):
        
        assert 0

    def test_getTotalReps(self):

        assert 0

    def test_getSuccessRate(self, test_data):
        exercise, rep, weight = 'Snatch', 3, 30.0
        assert self.dh.getSuccessRate(test_data, exercise, rep) == 0.89

    def test_getExerciseMaxAverage(self, test_data):
        exercise, rep, weight = 'Snatch', 3, 30.0
        assert self.dh.getExerciseMaxAverage(test_data, exercise, rep) == weight

    def test_getExerciseMax(self, test_data):
        exercise, rep, weight = 'Snatch', 1, 30.0
        assert self.dh.getExerciseMax(test_data, exercise, rep) == weight

    def test_getExerciseMaxes(self):
        
        assert 0

    def test_getCompetitionDates(self):
        
        assert 0

    def test_getPeriodDates(self):
        
        assert 0