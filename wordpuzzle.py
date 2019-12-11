#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is my first Python program!
* Yay!
@{link __main__}
"""

from utils.helpers import is_present, validation

#
# MAIN
#
if __name__ == '__main__':
    print('Word Puzzle')
    LETTERS = 'aptlyronh'
    DICT_WORD = 'python'
    MANDATORY_CHAR = 'o'
    MIN_LENGTH = 4

    WORD = DICT_WORD

    if validation(DICT_WORD, MANDATORY_CHAR, MIN_LENGTH):
        if is_present(LETTERS, DICT_WORD):
            print('Letters are present in dictionary word {}\n'.format(WORD))
        else:
            print(
                'Letters are NOT present in dictionary word {}\n'.format(WORD))
