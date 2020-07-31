#! python3

from data.dataHandler import DataHandler
import pandas

testDataFrame = pandas.DataFrame({'Date': ['2020-06-01', '2020-06-01', '2020-06-01', '2020-06-01', '2020-06-01'], 'Exercise': ['Snatch', 'Snatch', 'Snatch', 'Snatch', 'Snatch'], 'Reps': [1, 2, 3, 4, 5], 'Weight': [10, 20, 30, 40, 50]})

class Test_DataHandler():

    def setup_method(self):
        self.dh = DataHandler()
    
    def teardown_method(self):
        self.dh = None

    def test_getExercises(self):

        exercises = ['Snatch']
        assert self.dh.getExercises(testDataFrame) == exercises

    def test_getExerciseMaxAverage(self):

        exercise, rep, weight = 'Snatch', 5, 50.0
        assert self.dh.getExerciseMaxAverage(testDataFrame, exercise, rep) == weight

    def test_getExerciseMax(self):

        exercise, rep, weight = 'Snatch', 1, 10.0
        assert self.dh.getExerciseMax(testDataFrame, exercise, rep) == weight

    def test_getExerciseMaxes(self):

        exercise, rep, weight = 'Snatch', 5, 50.0
        assert self.dh.getExerciseMaxAverage(testDataFrame, exercise, rep) == weight