import unittest
from app.models import Comments

class CommentsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Comments
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = Comments()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comments)))
