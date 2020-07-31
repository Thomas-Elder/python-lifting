#! python3

from data.dataHandler import dataHandler
import pandas

testDataFrame = pandas.DataFrame({'Date': ['2020-06-01', '2020-06-01', '2020-06-01', '2020-06-01', '2020-06-01'], 'Exercise': ['Snatch', 'Snatch', 'Snatch', 'Snatch', 'Snatch'], 'Reps': [1, 2, 3, 4, 5], 'Weight': [10, 20, 30, 40, 50]})

def test_getExercises():

    dh = dataHandler()
    exercises = ['Snatch']
    assert dh.getExercises(testDataFrame) == exercises

def test_getExerciseMaxAverage():

    dh = dataHandler()
    exercise, rep, weight = 'Snatch', 5, 50.0
    assert dh.getExerciseMaxAverage(testDataFrame, exercise, rep) == weight

def test_getExerciseMax():

    dh = dataHandler()
    exercise, rep, weight = 'Snatch', 1, 10.0
    assert dh.getExerciseMax(testDataFrame, exercise, rep) == weight

def test_getExerciseMaxes():

    dh = dataHandler()
    exercise, rep, weight = 'Snatch', 5, 50.0
    assert dh.getExerciseMaxAverage(testDataFrame, exercise, rep) == weight