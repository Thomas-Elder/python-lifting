#! python3

# imports
from data.models.session import Session, Exercise, Set

import csv
import os 
from datetime import datetime

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

class DataReader:

    def __init__(self, file: str):
        
        logging.debug('initialising DataReader... ')
        logging.debug('cwd: %s' % (os.getcwd()))
        self.file = file
        self.dataset = []

        with open(file, mode='r', newline='') as csv_file:
            self.reader = csv.reader(csv_file)

            for data in self.reader:
                self.dataset.append(data)

        self.sessions = self.translateData(self.dataset, self.translateRepetitions)
        logging.debug('DataReader initialised')
    
    def translateData(self, dataset: list, repetitionTranslator):
        ''' Converts a list of csv data into a list of Session objects

        Parameters
        ----------
        dataset: a list

        Returns
        -------
        A list of Session objects
        '''
        logging.debug('translating data... ')

        dates = list(set([x[0] for x in dataset]))
        dates.sort()
        sessions = [Session(datetime.strptime(date, '%Y-%m-%d')) for date in dates]

        for session in sessions:

            # Get all the exercises for this date
            exercisesForDate = list(set([data[1] for data in dataset if datetime.strptime(data[0], '%Y-%m-%d') == session.date]))
            exercisesForDate.sort()
            # Add them to the sessions' exercise list
            session.exercises = [Exercise(exercise) for exercise in exercisesForDate]
        
            for exercise in session.exercises:
                
                # Get all the sets for this session's date, for this exercise               
                exerciseSets = [data for data in dataset if datetime.strptime(data[0], '%Y-%m-%d') == session.date and data[1] == exercise.name]

                # add set to the exercise for each row with this exercise and date
                for exerciseSet in exerciseSets:
                    totalRepetitions, successfulRepetitions, failedRepetitions = repetitionTranslator(exerciseSet[2])
                    exercise.sets.append(Set(totalRepetitions, successfulRepetitions, failedRepetitions, int(exerciseSet[3])))

                    # while we're here, let's check if any sets have an attempt value, if so, mark this session as a competition one
                    if exerciseSet[4] != '':
                        session.competition = True

        logging.debug('data translated')
        return sessions

    def translateRepetitions(self, repetitionString: str):
        ''' Converts a str a tuple of 3 ints representing the repetitions

        Parameters
        ----------
        repetitionString: a str

        Returns
        -------
        tuple of 3 values, totalRepetitions, successfulRepetitions, failedRepetitions
        '''
        logging.debug('translating repetitions... ')

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

        logging.debug('repetitions translated')
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

        #mask = (self.dataset['Date'] >= fromDate) & (self.dataset['Date'] <= toDate)
        return 0 
        #self.dataset.loc[mask] 