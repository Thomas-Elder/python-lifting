
# imports
from data.models.session import Session
from data.models.exercise import Exercise

from datetime import datetime

# logging
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Test_Session():

    def setup_method(self):
        logging.info('Setting up before test... ')
        self.session = Session(datetime(2020, 4, 1))
        self.session.addExercise(Exercise('Snatch', 'Snatch'))

    def teardown_method(self):
        logging.info('Tearing down after test... ')
        self.session = None

    def test_session(self):
        expected = 'Snatch'
        result = self.session.exercises

        for key in result.keys():
            assert key == expected
    