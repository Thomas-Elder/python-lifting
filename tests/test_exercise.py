
# imports
from data.models.exercise import Exercise
from data.models.set import Set

# logging
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Test_Exercise():

    def setup_method(self):
        logging.info('Setting up before test... ')
        
        self.exercise = Exercise('Snatch')
        self.exercise.sets = [Set(3, 2, 1, 30), Set(3, 3, 3, 30), Set(3, 3, 3, 60)]

    def teardown_method(self):
        logging.info('Tearing down after test... ')
        self.set = None

    def test_exercise(self):
        assert self.exercise.name == 'Snatch'
        #assert self.exercise.sets[0].totalRepetitions == 3

    def test_totalWeight(self):
        
        expected = 360
        result = self.exercise.totalWeight()

        assert result == expected

    def test_numberOfSets(self):
        pass

    def test_numberOfReps(self):
        pass

    def test_topSet(self):
        pass