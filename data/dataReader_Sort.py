#! python3

# imports
from data.models.session import Session, Exercise, Set

import csv
import os 
from datetime import datetime
from timeit import default_timer as timer

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

class DataReader_Sort:

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

        start = timer()
        sessions = [Session(datetime.strptime(date, '%Y/%m/%d')) for date in dates]
        end = timer()
        print(f'Sessions comprehension exection time: {round(end-start, 2)} seconds') #  0 seconds
        print(f'Number of sessions: {len(sessions)}')

        for session in sessions:

            start = timer()
            # Get all the exercises for this date
            uniqueExercisesForDate = list({data[1]: data for data in dataset if datetime.strptime(data[0], '%Y/%m/%d') == session.date}.values())

            # this sort of does nothing rn, I'm not sure sort on strings is alphabetical by default or not? 
            uniqueExercisesForDate.sort(key=lambda x: x[1], reverse=True)

            # Add them to the sessions' exercise list
            session.exercises = [Exercise(exercise[1], exercise[5]) for exercise in uniqueExercisesForDate]
            end = timer()
            print(f'Getting exercises for date, and adding them to session exection time: {round(end-start, 2)} seconds') # 0.01 seconds but for every session. 118 sessions atm.

            start = timer()
            for exercise in session.exercises:
                
                # Get all the sets for this session's date, for this exercise               
                exerciseSets = [data for data in dataset if datetime.strptime(data[0], '%Y/%m/%d') == session.date and data[1] == exercise.name]

                # add set to the exercise for each row with this exercise and date
                for exerciseSet in exerciseSets:
                    totalRepetitions, successfulRepetitions, failedRepetitions = repetitionTranslator(exerciseSet[2])
                    exercise.sets.append(Set(totalRepetitions, successfulRepetitions, failedRepetitions, int(exerciseSet[3])))

                    # while we're here, let's check if any sets have an attempt value, if so, mark this session as a competition one
                    if exerciseSet[4] != '':
                        session.competition = True

            end = timer()
            print(f'Organising exercises and sets exection time: {round(end-start, 2)} seconds') # ~0.04-0.1 seconds

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

        if 'x' not in repetitionString.lower():
            total += int(repetitionString)
            successful += int(repetitionString)

        else: 
            for char in repetitionString:

                if char.lower() == 'x':
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