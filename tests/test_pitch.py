import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(id=1, title = 'general',pitch_content = 'I will not give up nor will will i give in', category = 'Pickup Line',author = 'Maggy', likes = True, dislikes = False) 

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))