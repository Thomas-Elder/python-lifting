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
    '''Computes the average session maximum weight lifted for the given exercise and rep number.
    
    Parameters
    ----------
    exercise: str
    reps: int
    '''

    exercise_maxes = []

    for date in dataset['Date'].unique():

        logging.debug('Exercise being searched: %s' % (exercise))

        # get the sets for this date
        sets = dataset[dataset['Date'] == date]
        #logging.debug('sets: %s' % (sets))

        # get sets with given exercise
        exercise_sets = sets[sets['Exercise'] == exercise]
        logging.debug('exercise_sets: \n%s' % (exercise_sets))

        # get sets with given rep number
        exercise_sets_reps = exercise_sets[exercise_sets['Reps'] == reps]
        logging.debug('exercise_sets_reps: \n%s' % (exercise_sets_reps))

        # get max weight
        exercise_max = exercise_sets_reps['Weight'].max()
        logging.debug('exercise_max: \n%s' % (exercise_max))

        exercise_maxes.append(exercise_max)

    clean_maxes = [x for x in exercise_maxes if str(x) != 'nan']
    logging.debug('exercise_maxes: \n%s' % (clean_maxes))

    exercise_average = statistics.mean(clean_maxes)
    logging.debug('exercise_average: \n%s' % (exercise_average))

    return exercise_average

def getExerciseMax(exercise: str, reps: int) -> float:
    '''Finds the highest weight lifted for the given exercise and rep number.
    
    Parameters
    ----------
    exercise: str
    reps: int
    '''

    logging.debug('Exercise being searched: %s' % (exercise))

    # get sets with given exercise
    exercise_sets = dataset[dataset['Exercise'] == exercise]
    logging.debug('exercise_sets: \n%s' % (exercise_sets))

    # get sets with given rep number
    exercise_sets_reps = exercise_sets[exercise_sets['Reps'] == reps]
    logging.debug('exercise_sets_reps: \n%s' % (exercise_sets_reps))

    # get max weight
    exercise_max = exercise_sets_reps['Weight'].max()
    logging.debug('exercise_max: \n%s' % (exercise_max))

    return exercise_max

def getExerciseMaxes(exercise: str, reps: int) -> list:
    '''Finds the all the top set weights lifted for the given exercise and rep number.
    
    Parameters
    ----------
    exercise: str
    reps: int

    Returns
    -------
    A list of dictionaries containing all the max weights lifted in each session, eg
    [{'date': '25Jul20', 'weight': 80}]
    '''

    exercise_maxes = []

    for date in dataset['Date'].unique():

        logging.debug('Exercise being searched: %s' % (exercise))

        # get the sets for this date
        sets = dataset[dataset['Date'] == date]
        #logging.debug('sets: %s' % (sets))

        # get sets with given exercise
        exercise_sets = sets[sets['Exercise'] == exercise]
        logging.debug('exercise_sets: \n%s' % (exercise_sets))

        # get sets with given rep number
        exercise_sets_reps = exercise_sets[exercise_sets['Reps'] == reps]
        logging.debug('exercise_sets_reps: \n%s' % (exercise_sets_reps))

        # get max weight
        exercise_max = {'date': date, 'weight': exercise_sets_reps['Weight'].max()}
        logging.debug('exercise_max: \n%s' % (exercise_max))

        exercise_maxes.append(exercise_max)

    clean_maxes = [x for x in exercise_maxes if str(x['weight']) != 'nan']
    logging.debug('exercise_maxes: \n%s' % (clean_maxes))

    return clean_maxes

print()
print('Snatch max 1 rep: %s' % (getExerciseMax('Snatch', 1)))
print('Clean and Jerk max 1 rep: %s' % (getExerciseMax('Clean and Jerk', 1)))
print()
print('Snatch Pulls average top set 3 reps: %s' % (getExerciseMaxAverage('Snatch Pull', 3)))
print('Clean Pulls average top set 3 reps: %s' % (getExerciseMaxAverage('Clean Pull', 3)))
print('Front Squats average top set 3 reps: %s' % (getExerciseMaxAverage('Front Squat', 3)))
print('Back Squats average top set 3 reps: %s' % (getExerciseMaxAverage('Back Squat', 3)))
print('Power Snatch average top set 3 reps: %s' % (getExerciseMaxAverage('Power Snatch', 3)))
print('Power Clean average top set 3 reps: %s' % (getExerciseMaxAverage('Power Clean', 3)))
print('Snatch Balance average top set 1 rep: %s' % (getExerciseMaxAverage('Snatch Balance', 1)))
print()
print('Snatch Pulls top sets 3 reps: %s' % (getExerciseMaxes('Snatch Pull', 3)))