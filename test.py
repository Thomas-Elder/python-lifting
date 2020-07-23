#! python3

import pandas

import os 
import statistics

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

logging.debug('cwd: %s' % (os.getcwd()))
dataset = pandas.read_csv('lifting_data.csv')


def getExerciseMaxAverage(exercise: str, reps: int) -> float:
    '''Computes the average session maximum weight lifted for the given exercise and rep number.'''

    exercise_maxes = []

    for date in dataset['Date'].unique():

        logging.debug('Exercise being searched: %s' % (exercise))

        # get the sets for this date
        sets = dataset[dataset['Date'] == date]
        #logging.debug('sets: %s' % (sets))

        # get any snatch pull sets that happened on this date
        exercise_sets = sets[sets['Exercise'] == exercise]
        logging.debug('exercise_sets: \n%s' % (exercise_sets))

        # we want only the sets with reps of 3
        exercise_sets_reps = exercise_sets[exercise_sets['Reps'] == reps]
        logging.debug('exercise_sets_reps: \n%s' % (exercise_sets_reps))

        # we want to add only the highest snatch pull weight
        exercise_max = exercise_sets_reps['Weight'].max()
        logging.debug('exercise_max: \n%s' % (exercise_max))

        exercise_maxes.append(exercise_max)

    clean_maxes = [x for x in exercise_maxes if str(x) != 'nan']
    logging.debug('exercise_maxes: \n%s' % (clean_maxes))

    exercise_average = statistics.mean(clean_maxes)
    logging.debug('exercise_average: \n%s' % (exercise_average))

    return exercise_average

print('Snatch: %s' % (getExerciseMaxAverage('Snatch', 1)))
print('Clean and Jerk: %s' % (getExerciseMaxAverage('Clean and Jerk', 1)))
print('Snatch Pulls: %s' % (getExerciseMaxAverage('Snatch Pull', 3)))
print('Clean Pulls: %s' % (getExerciseMaxAverage('Clean Pull', 3)))
print('Front Squats: %s' % (getExerciseMaxAverage('Front Squat', 3)))
print('Back Squats: %s' % (getExerciseMaxAverage('Back Squat', 3)))
print('Power Snatch: %s' % (getExerciseMaxAverage('Power Snatch', 3)))
print('Power Clean: %s' % (getExerciseMaxAverage('Power Clean', 3)))
print('Snatch Balance: %s' % (getExerciseMaxAverage('Snatch Balance', 1)))