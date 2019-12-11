#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Please add me!
"""
import unittest

from utils.helpers import is_present, validation


class TestIsPresent(unittest.TestCase):
    '''Test word puzzle utility functions.'''

    def test_is_present(self):
        ''' Word contains valid characters. '''
        self.assertTrue(is_present('haisjdlfk', 'hi'))

    def test_validation(self):
        '''Dictionary words validated for length and mandatory character'''
        self.assertTrue(validation('book', 'k', 4))

    def test_mandatory_character(self):
        '''Mandatory character present validation'''
        self.assertFalse(validation('book', 'a', 4))

    def test_minimum_length(self):
        '''Minimum length validation'''
        self.assertFalse(validation('boo', 'b', 4))
