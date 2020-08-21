
# imports
from data.models.set import Set

# logging
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Test_Set():

    def setup_method(self):
        logging.info('Setting up before test... ')
        self.set = Set(3, 2, 1, 30)

    def teardown_method(self):
        logging.info('Tearing down after test... ')
        self.set = None

    def test_set(self):
        assert self.set.totalRepetitions == 3
        assert self.set.successfulRepetitions == 2
        assert self.set.failedRepetitions == 1