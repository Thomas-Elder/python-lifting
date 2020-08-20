
# imports
from data.models.session import Session
from data.models.exercise import Exercise

import pandas

# logging
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Test_Session():

    def setup_method(self):
        logging.info('Setting up before test... ')
        self.session = Session(pandas.to_datetime('2020-04-01'))
        self.session.addExercise(Exercise('Snatch'))

    def teardown_method(self):
        logging.info('Tearing down after test... ')
        self.session = None

    def test_getDate(self):
        expected = pandas.to_datetime('2020-04-01')
        result = self.session.getDate()

        assert result == expected

    def test_session(self):
        expected = 'Snatch'
        result = self.session.exercises[0].name

        assert result == expected
    