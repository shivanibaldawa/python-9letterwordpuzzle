#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is my first Python program!
* Yay!
@{link __main__}
"""

from utils.helpers import is_present

#
# MAIN
#
if __name__ == '__main__':
    print('Word Puzzle')
    LETTERS = 'aptlyronh'
    DICT_WORD = 'python'
    if is_present(LETTERS, DICT_WORD):
        print('Letters are present in dictionary word "{}"\n'.format(DICT_WORD))
    else:
        print(
            'Letters are NOT present in dictionary word "{}"\n'.format(DICT_WORD))
