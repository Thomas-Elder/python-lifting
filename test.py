#! python3

import pandas

import os 

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

logging.debug('cwd: %s' % (os.getcwd()))
dataset = pandas.read_csv('lifting_data.csv')