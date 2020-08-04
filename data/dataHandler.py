#! python3

import pandas

import os 
import statistics
import numpy
from datetime import datetime, timedelta

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

            # get the max weight for this date, exercise and reps
            exercise_max = dataset[(dataset['Date'] == date) & (dataset['Exercise'] == exercise) & (dataset['Reps'] == reps)].max()['Weight']

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

        return dataset.loc[(dataset['Exercise'] == exercise) & (dataset['Reps'] == reps)].max()['Weight']

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

            # get the sets with max weight for this exercise on this date, with this number of reps
            maxweight = dataset[(dataset['Date'] == date) & (dataset['Exercise'] == exercise) & (dataset['Reps'] == reps)].max()

            # append to the list
            exercise_maxes.append({'Date': maxweight['Date'], 'Weight': maxweight['Weight']})

        # clear out all the nans.
        clean_maxes = [x for x in exercise_maxes if str(x['Weight']) != 'nan']

        return clean_maxes

    def getCompetitionDates(self, dataset) -> list:
        '''Finds the all the dates of competition.
        
        Finds sets with an attempt number and returns the dates when those sets occured.

        Parameters
        ----------
        dataset: a pandas dataFrame

        Returns
        -------
        A list of numpy datetime objects
        '''

        competitionSets = dataset.loc[dataset['Attempt'] != 0]
        return competitionSets['Date'].unique()

    def getPeriodDates(self, dataset, competitionDates) -> list:
        '''Gets a list of tuples of the start/end date of training periods
        
        For the given competition dates, returns start/end dates of the periods
        between competitions.

        Parameters
        ----------
        dataset: a pandas dataFrame
        competitionDates: a list of strings representing competition dates

        Returns
        -------
        A list of tuples of two strings, the start and end date
        '''

        trainingPeriods = []

        # First we need the earliest and latest date in the list.
        start = min(dataset['Date'])
        end = max(dataset['Date'])

        print('competitionDates[0] - pandas.Timedelta(1): {}'.format(competitionDates[0] - pandas.Timedelta(days=1)))

        # The first period will be from the start to the first comp:
        trainingPeriods.append((start, competitionDates[0] - pandas.Timedelta(days=1)))

        # If there's only one comp, we can just toss on the last period now
        if len(competitionDates) == 1:
            trainingPeriods.append((competitionDates[0] + pandas.Timedelta(days=1), end))

        # Otherwise we need to loop over dates to get all the periods
        else:
            for i in range(len(competitionDates) - 1):
                # Then we need to loop over compdates:
                trainingPeriods.append((competitionDates[i] + pandas.Timedelta(days=1), competitionDates[i + 1] - pandas.Timedelta(days=1)))

            # Then add the last period from last comp to end.
            trainingPeriods.append((competitionDates[len(competitionDates) - 1] + pandas.Timedelta(days=1), end))

        return trainingPeriods