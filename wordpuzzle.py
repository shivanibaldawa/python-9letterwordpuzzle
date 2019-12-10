#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is my first Python program!
* Yay!
@{link __main__}
"""

#
# GLOBALS
#


def is_present(letters, dict_word):
    ''' Please add pydoc. '''
    word = dict_word[:]
    for i in letters:
        if word.__contains__(i):
            word.remove(i)
            if len(word) == 0:
                return True
    return False


#
# MAIN
#
if __name__ == '__main__':
    print('Word Puzzle')
    LETTERS = list('aptlyronh')
    DICT_WORD = list('python')
    WORD = DICT_WORD
    if is_present(LETTERS, DICT_WORD):
        print('Letters are present in dictionary word {}\n'.format(WORD))
    else:
        print('Letters are NOT present in dictionary word {}\n'.format(WORD))
