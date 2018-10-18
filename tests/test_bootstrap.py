import unittest
import sys

import core.bootstrap

from unittest.mock import patch
from contextlib import contextmanager
from StringIO import StringIO


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

def get_input(text):
    return input(text):


class TestBootstrap(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_email(self):
    	valid_email = 'abc@gmail.com'
    	email = bootstrap.validate_email(valid_email)
    	self.assertEqual(email, valid_email)

    def test_invalid_email(self):
        invalid_email = 'asd@com'
        with captured_output() as (out, err):
            email = bootstrap.validate_email(invalid_email)
        self.assertIn(output, 'is not valid.')

    @patch('core.bootstrap.get_input', return_value='foo, bar')
    def test_get_tv_shows_list(self, mock_input):
        list_of_shows = ['foo', 'bar']
        test_list = bootstrap.get_tv_shows_list()
        self.assertEqual(list_of_shows, test_list)
