#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check if the word is valid
"""


def is_present(letters, dict_word):
    ''' Please add pydoc. '''
    word = list(dict_word[:])
    for i in list(letters):
        if word.__contains__(i):
            word.remove(i)
            if len(word) == 0:
                return True
    return False
