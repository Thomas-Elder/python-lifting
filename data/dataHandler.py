#! python3

import pandas

import os 
import statistics
from datetime import datetime

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

class DataHandler:

    def getExercises(self, dataset) -> list:
        '''Returns a list of exercises from the given dataset

        Parses the dataframe and compiles a list of unique Exercises.

        Parameters
        ----------
        dataset: a pandas dataframe

        Returns
        -------
        The exercises as a list of strings
        '''
        
        return dataset['Exercise'].unique()

    def getExerciseMaxAverage(self, dataset, exercise: str, reps: int) -> float:
        '''Computes the average session maximum weight lifted for the given exercise and rep number.
        
        Parameters
        ----------
        dataset: a pandas dataFrame
        exercise: str
        reps: int

        Returns
        -------
        A float, the average of all max weights for the given exercise and number of reps
        '''

        exercise_maxes = []

        for date in dataset['Date'].unique():

            logging.debug('Exercise being searched: %s' % (exercise))

            # get the sets for this date
            sets = dataset[dataset['Date'] == date]

            # get sets with given exercise
            exercise_sets = sets[sets['Exercise'] == exercise]

            # get sets with given rep number
            exercise_sets_reps = exercise_sets[exercise_sets['Reps'] == reps]

            # get max weight
            exercise_max = exercise_sets_reps['Weight'].max()

            # add exercise to the list
            exercise_maxes.append(exercise_max)

        # clean empty elements
        clean_maxes = [x for x in exercise_maxes if str(x) != 'nan']

        if len(clean_maxes) > 0:
            exercise_average = statistics.mean(clean_maxes)
            return exercise_average

        return 0

    def getExerciseMax(self, dataset, exercise: str, reps: int) -> float:
        '''Finds the highest weight lifted for the given exercise and rep number.
        
        Parameters
        ----------
        dataset: a pandas dataFrame
        exercise: str
        reps: int

        Returns
        -------
        A float, the max weight lifted for the given exercise and number of reps
        '''

        logging.debug('Exercise being searched: %s' % (exercise))

        # get sets with given exercise
        exercise_sets = dataset[dataset['Exercise'] == exercise]

        # get sets with given rep number
        exercise_sets_reps = exercise_sets[exercise_sets['Reps'] == reps]

        # get max weight
        exercise_max = exercise_sets_reps['Weight'].max()

        return exercise_max

    def getExerciseMaxes(self, dataset, exercise: str, reps: int) -> list:
        '''Finds the all the top set weights lifted for the given exercise and rep number.
        
        Parameters
        ----------
        dataset: a pandas dataFrame
        exercise: str
        reps: int

        Returns
        -------
        A list of dictionaries containing all the max weights lifted in each session, eg
        [{'date': '25Jul20', 'weight': 80}]

        for the given exercise and number of reps.
        '''

        exercise_maxes = []

        for date in dataset['Date'].unique():

            logging.debug('Exercise being searched: %s' % (exercise))

            # get the sets for this date
            sets = dataset[dataset['Date'] == date]

            # get sets with given exercise
            exercise_sets = sets[sets['Attempts'] != '']

            # get sets with given rep number
            exercise_sets_reps = exercise_sets[exercise_sets['Reps'] == reps]

            # get max weight
            exercise_max = {'date': date, 'weight': exercise_sets_reps['Weight'].max()}

            exercise_maxes.append(exercise_max)

        clean_maxes = [x for x in exercise_maxes if str(x['weight']) != 'nan']

        return clean_maxes

    def getCompetitionDates(self, dataset) -> list:
        
        competitionSets = dataset.loc[dataset['Attempt'] != '']

        return competitionSets['Date'].unique()