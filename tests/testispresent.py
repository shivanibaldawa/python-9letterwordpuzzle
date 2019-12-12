#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests the utility functions of the Wordpuzzle
"""
import unittest

from utils.helpers import is_present, mandatorychar_check, minimumlength_check


class TestIsPresent(unittest.TestCase):
    '''Test word puzzle utility functions.'''

    def test_is_present(self):
        ''' Word contains valid characters. '''
        self.assertTrue(is_present('haisjdlfk', 'hi'))

    def test_is_not_present(self):
        '''Word contains invalid characters'''
        self.assertFalse(is_present('alsbcjsie', 'hi'))

    def test_mandatorychar_present(self):
        '''Mandatory character is present in the dictionary word'''
        self.assertTrue(mandatorychar_check('book', 'k'))

    def test_mandatorychar_absent(self):
        '''Mandatory character is absent in the dictionary word'''
        self.assertFalse(mandatorychar_check('book', 'a'))

    def test_minimumlength(self):
        '''Character is of the minimum length'''
        self.assertTrue(minimumlength_check('book', 4))

    def test_notminimumlength(self):
        '''Character is of the minimum length'''
        self.assertFalse(minimumlength_check('boo', 4))
