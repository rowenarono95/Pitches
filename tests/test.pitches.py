from ..models import Comment,User,Pitch
from app import db
import unittest

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_rono = User(username = 'rono',password = 'banana', email = 'rowenarono@gmail.com')
        self.new_pitch = Pitch(id=1,pitch_comment='This is a test pitch',category="interview",user = self.user_rono,likes=0,dislikes=0)

    def tearDown(self):
        User.query.delete()
        Pitch.query.delete()
      

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_comment,'This is a test pitch')
        self.assertEquals(self.new_pitch.category,"interview")
        self.assertEquals(self.new_pitch.user,self.user_rono)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitch(1)
        self.assertTrue(got_pitch is not None)
