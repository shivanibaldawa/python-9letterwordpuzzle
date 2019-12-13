#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is my first Python program!
* Yay!
@{link __main__}
"""
import argparse
import sys
from utils.helpers import is_present, mandatorychar_check, minimumlength_check

#
# MAIN
#
if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(
        description=
        'Process letters,minimumlength, mandatory character and dictionary')

    PARSER.add_argument('-l',
                        '--letters',
                        required=True,
                        help='9 letters to create words from')

    PARSER.add_argument('-c',
                        '--mandatorycharacter',
                        required=True,
                        help='Mandatory character to be present in the words')

    PARSER.add_argument(
        '-m',
        '--minimumlength',
        type=int,
        default=4,
        help='Minimum length of the dictionary words formed. Default is 4.')

    #PARSER.parse_args('Dictionary.txt',type=argparse.FileType('r'))
    PARSER.add_argument('-d',
                        '--Dictionary',
                        type=argparse.FileType('r'),
                        default='Dictionary.txt')

    ARGS = PARSER.parse_args()

    if 1 <= ARGS.minimumlength <= 9:
        MIN_LENGTH = ARGS.minimumlength
    else:
        print('Minimum length should be in the range of 1 to 9')
        sys.exit(1)

    if (len(ARGS.letters) == 9 and ARGS.letters.isalpha()):
        LETTERS = ARGS.letters.lower()
    else:
        print('Letters should be 9 valid characters')
        sys.exit(1)

    if len(ARGS.mandatorycharacter) == 1 and ARGS.mandatorycharacter.isalpha():
        MANDATORY_CHAR = ARGS.mandatorycharacter.lower()
    else:
        print('Mandatory character should be a valid one character')
        sys.exit(1)

    for DICT_WORD in ARGS.Dictionary:
        WORD = DICT_WORD.strip()
        if mandatorychar_check(WORD, MANDATORY_CHAR) and minimumlength_check(
                WORD, MIN_LENGTH) and is_present(LETTERS,
                                                 WORD) and len(DICT_WORD) <= 9:
            print(WORD)
