#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validation fo the letters and the dictionary word
"""


def mandatorychar_check(dict_word, mandatory_char):
    '''Checks if the dictionary word has the valid character present in it'''
    if dict_word.__contains__(mandatory_char):
        return True
    return False


def minimumlength_check(dict_word, minimum_length):
    '''Checks if the dictionary word satisfies the condition of the minimum length'''
    if len(dict_word) >= minimum_length:
        return True
    return False


def is_present(letters, dict_word):
    ''' Checks if the letters are present in the dictionary word '''
    word = list(dict_word[:])
    for i in list(letters):
        if word.__contains__(i):
            word.remove(i)
            if len(word) == 0:
                return True
    return False
