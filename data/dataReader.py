#! python3

# imports
from data.models.session import Session, Exercise, Set

import pandas

import os 
from datetime import datetime

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

class DataReader:

    def __init__(self, file: str):
        
        logging.debug('cwd: %s' % (os.getcwd()))
        self.file = file
        self.dataset = pandas.read_csv(self.file)
        self.dataset['Attempt'] = self.dataset['Attempt'].fillna(0)
        self.dataset['Date'] = pandas.to_datetime(self.dataset['Date'])
        self.sessions = []
    
    def translateData(self, dataset: pandas.DataFrame, repetitionTranslator):
        ''' Converts a pandas DataFrame into a list of session objects

        Uses dubious pandas anti-patterns to convert the dataframe into a more
        comprehensible (for me) list of session objects, with associated
        exercise and set objects.

        Parameters
        ----------
        dataset: a pandas dataFrame

        Returns
        -------
        None
        '''

        dates = dataset['Date'].unique()

        self.sessions = [Session(date) for date in dates]

        for session in self.sessions:

            exercisesForDate = dataset[dataset['Date'] == session.date]['Exercise'].unique()
            session.exercises = [Exercise(exercise) for exercise in exercisesForDate]
        
            for exercise in session.exercises:
                
                # Get all the sets for this session's date, for this exercise
                exerciseSets = dataset[(dataset['Date'] == session.date) & (dataset['Exercise'] == exercise.name)].values.tolist()
                
                # add set to the exercise for each row with this exercise and date
                for exerciseSet in exerciseSets:
                    totalRepetitions, successfulRepetitions, failedRepetitions = repetitionTranslator(exerciseSet[2])
                    exercise.sets.append(Set(totalRepetitions, successfulRepetitions, failedRepetitions, exerciseSet[3]))

    def translateRepetitions(self, repetitionString: str):
        ''' Converts a str a tuple of 3 ints representing the repetitions

        Parameters
        ----------
        repetitionString: a str

        Returns
        -------
        tuple of 3 values, totalRepetitions, successfulRepetitions, failedRepetitions
        '''

        total, successful, failed = 0, 0, 0

        if 'X' not in repetitionString:
            total += int(repetitionString)
            successful += int(repetitionString)

        else: 
            for char in repetitionString:

                if char == 'X':
                    failed += 1
                    total += 1
                else:
                    successful += int(char)
                    total += int(char)

        return (total, successful, failed)

    def getData(self, fromDate=None, toDate=None):
        '''Returns a dataframe containing sets between the specified dates
    
        If fromDate or toDate are not specified returns the entire dataset.

        Parameters
        ----------
        fromDate: str of format 2020-06-01
        toDate: str of format 2020-06-01

        Returns
        -------
        A pandas dataFrame
        '''
        
        if fromDate == None or toDate == None:
            return self.dataset

        mask = (self.dataset['Date'] >= fromDate) & (self.dataset['Date'] <= toDate)
        return self.dataset.loc[mask] 