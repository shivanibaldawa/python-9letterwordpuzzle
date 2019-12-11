
import unittest
#from wordpuzzle.ispresent import is_present
from utils.ispresent import ispresent


class testispresent(unittest.TestCase):

    def test_is_present(self):
        self.assertTrue(is_present('haisjdlfk', 'hi'))
