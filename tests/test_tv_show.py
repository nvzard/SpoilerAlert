import sys
import unittest


from core.TVShow.TVShow import TVShow


class TestTVShow(unittest.TestCase):

    def test_get_show_url(self):
        show_name = 'foo bar'
        show_url = 'https://next-episode.net/foo-bar'
        self.assertEqual(show_url, TVShow.get_show_url(show_name))

    def test_find_value(self):
        test_string = ('This is a raw text with a HIDDEN_KEY'
                        'and some swag.\n ans some rubbish')
        test_key = 'HIDDEN_KEY'
        return_value = 'HIDDEN_KEY and some swag.'
        self.assertEqual(return_value, TVShow.findValue(test_key, test_string))
