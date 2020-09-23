#! python3

# Imports
import pytest

from data.dataHandler import DataHandler
from data.models.session import Session
from data.models.exercise import Exercise
from data.models.set import Set

from datetime import datetime

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def test_data():
    testSessions = []

    testSessions.append(Session(datetime.strptime('2020-04-01', '%Y-%m-%d')))

    exercises = []

    exercises.append(Exercise('Snatch', 'Snatch'))
    exercises.append(Exercise('Clean and Jerk', 'Clean and Jerk'))

    exercises[0].sets = [Set(3, 2, 1, 30), Set(1, 1, 0, 10), Set(2, 2, 0, 20), Set(3, 3, 0, 15)]
    exercises[1].sets = [Set(3, 2, 1, 50), Set(3, 3, 0, 20), Set(3, 3, 0, 30), Set(3, 3, 0, 45)]

    testSessions[0].addExercise(exercises[0])
    testSessions[0].addExercise(exercises[1])

    testSessions.append(Session(datetime.strptime('2020-05-01', '%Y-%m-%d')))
    testSessions[1].competition = True

    exercises = []

    exercises.append(Exercise('Snatch', 'Snatch'))
    exercises.append(Exercise('Clean and Jerk', 'Clean and Jerk'))

    exercises[0].sets = [Set(1, 0, 1, 50), Set(1, 1, 0, 50), Set(1, 1, 0, 40), Set(1, 1, 0, 30)]
    exercises[1].sets = [Set(1, 0, 1, 70), Set(1, 1, 0, 60), Set(1, 1, 0, 50), Set(1, 1, 0, 40)]

    testSessions[1].addExercise(exercises[0])
    testSessions[1].addExercise(exercises[1])

    return testSessions

class Test_DataHandler():

    def setup_method(self):
        logging.info('Setting up before test... ')
        self.dh = DataHandler()

    def teardown_method(self):
        logging.info('Tearing down after test... ')
        self.dh = None

    def test_getSessionsNonCompetition(self, test_data):
        expected = [datetime.strptime('2020-04-01', '%Y-%m-%d')]
        result = self.dh.getSessions(test_data, datetime.strptime('2020-04-01', '%Y-%m-%d'), datetime.strptime('2020-04-30', '%Y-%m-%d'), competition=False)

        assert len(result) == len(expected)

        for i in range(len(result)):
            assert result[i].date == expected[i]

    def test_getSessionsCompetition(self, test_data):
        expected = [datetime.strptime('2020-05-01', '%Y-%m-%d')]
        result = self.dh.getSessions(test_data, datetime.strptime('2020-05-01', '%Y-%m-%d'), datetime.strptime('2020-05-30', '%Y-%m-%d'), competition=True)

        assert len(result) == len(expected)

        for i in range(len(result)):
            assert result[i].date == expected[i]

    def test_getExercises(self, test_data):
        exercises = ['Snatch', 'Clean and Jerk']
        assert self.dh.getExercises(test_data) == exercises

    def test_getSuccessRate(self, test_data):
        exercise, rep = 'Snatch', 3
        assert self.dh.getSuccessRate(test_data, exercise, rep) == 0.83

    def test_getExerciseMaxAverage(self, test_data):
        exercise, rep, weight = 'Snatch', 3, 30.0
        assert self.dh.getExerciseMaxAverage(test_data, exercise, rep) == weight

    def test_getExerciseMax(self, test_data):
        exercise, rep, weight = 'Snatch', 2, 20.0
        assert self.dh.getExerciseMax(test_data, exercise, rep) == weight

    def test_getExerciseMaxes(self, test_data):
        exercise, rep, weight = 'Snatch', 3, [{'date':datetime.strptime('2020-04-01', '%Y-%m-%d'), 'weight': 30.0}]
        assert self.dh.getExerciseMaxes(test_data, exercise, rep) == weight

    def test_getCompetitionDates(self, test_data):
        expected = [datetime.strptime('2020-05-01', '%Y-%m-%d')]
        assert self.dh.getCompetitionDates(test_data) == expected

    def test_getCompetitionPeriodDates(self, test_data):
        competitionDates = [datetime.strptime('2020-04-01', '%Y-%m-%d'), datetime.strptime('2020-07-01', '%Y-%m-%d')]
        expected = [(datetime.strptime('1986-03-24', '%Y-%m-%d'), datetime.strptime('2020-03-31', '%Y-%m-%d')), 
                    (datetime.strptime('2020-04-02', '%Y-%m-%d'), datetime.strptime('2020-06-30', '%Y-%m-%d')), 
                    (datetime.strptime('2020-07-02', '%Y-%m-%d'), datetime.strptime('2030-12-31', '%Y-%m-%d'))]
        
        result = self.dh.getCompetitionPeriodDates(competitionDates)
        assert result == expected