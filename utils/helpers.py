#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validation fo the letters and the dictionary word
"""


def validation(dict_word, mandatory_char, minimum_length):
    '''Validates the dictionary word to check if it has mandatory character and minimum length'''
    if (dict_word.__contains__(mandatory_char) and
            len(dict_word) >= minimum_length):
        return True
    return False


def is_present(letters, dict_word):
    ''' Please add pydoc. '''
    word = list(dict_word[:])
    for i in list(letters):
        if word.__contains__(i):
            word.remove(i)
            if len(word) == 0:
                return True
    return False
