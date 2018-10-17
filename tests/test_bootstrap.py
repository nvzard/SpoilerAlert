import unittest
from core.bootstrap import validate_email

class TestBootstrap(unittest.TestCase):

    def setUp(self):
        pass

    def test_validate_email(self):
    	valid_email = 'abc@gmail.com'
    	email = validate_email(valid_email)
    	self.assertEqual(email, valid_email)
