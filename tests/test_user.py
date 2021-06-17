import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(id = 1,  username = 'Milly', email="millyog@gmail.com", bio = 'i love all things premium', profile_pic_path='/photos/login.jpg',password = 'millyson',)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, User))

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('millyson'))