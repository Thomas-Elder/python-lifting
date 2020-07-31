#! python3

from data.dataHandler import dataHandler
import pandas

def test_getExerciseMax():
    testDataFrame = pandas.DataFrame({'Date': ['2020-06-01', '2020-06-01', '2020-06-01', '2020-06-01', '2020-06-01'], 'Exercise': ['Snatch', 'Snatch', 'Snatch', 'Snatch', 'Snatch'], 'Reps': [1, 2, 3, 4, 5], 'Weight': [10, 20, 30, 40, 50]})

    dh = dataHandler()

    assert dh.getExerciseMax(testDataFrame, 'Snatch', 1) == 10.0