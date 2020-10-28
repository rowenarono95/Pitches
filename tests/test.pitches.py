
        
        
import unittest
from app.models import Pitches

class PitchesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitches
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitches = Pitches()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitches))
