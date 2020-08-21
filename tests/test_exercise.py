
# imports
from data.models.exercise import Exercise
import pandas

# logging
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Test_Exercise():

    def setup_method(self):
        logging.info('Setting up before test... ')
        self.exercise = Exercise('Snatch')

    def teardown_method(self):
        logging.info('Tearing down after test... ')
        self.set = None

    def test_exercise(self):
        assert self.exercise.name == 'Snatch'