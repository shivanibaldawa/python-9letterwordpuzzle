#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is my first Python program!
* Yay!
@{link __is_present__}
"""


def is_present(letters, dict_word):
    ''' Please add pydoc. '''
    word = dict_word[:]
    for i in letters:
        if word.__contains__(i):
            word.remove(i)
            if len(word) == 0:
                return True
    return False
