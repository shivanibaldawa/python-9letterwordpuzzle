#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Please add me!
"""
import unittest

from utils.ispresent import is_present


class TestIsPresent(unittest.TestCase):
    ''' Test word puzzle utility functions. '''

    def test_is_present(self):
        ''' Word contains valid characters. '''
        self.assertTrue(is_present('haisjdlfk', 'hi'))
