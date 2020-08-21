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
    
    def translateData(self, dataset: pandas.DataFrame):

        for date in dataset['Date'].unique():

            session = Session(date)
            sessionData = dataset[dataset['Date'] == date]
            
            # add each element of sessionData to the session
            session.exercises = [Exercise(row.Exercise) for row in sessionData.itertuples()]

            # append all sessions to the sessions list
            self.sessions.append(session)

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