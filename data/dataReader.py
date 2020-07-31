#! python3

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
    
    def getData(self, fromDate='', toDate=''):
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
        
        if fromDate == '' or toDate == '':
            return self.dataset

        mask = (self.dataset['Date'] > fromDate) & (self.dataset['Date'] <= toDate)
        return self.dataset.loc[mask] 