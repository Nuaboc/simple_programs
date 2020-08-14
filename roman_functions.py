"""
A module with a series of functions to convert roman numerals to natural numbers and vice versa.

Author: Gabriel Martinez
Date: August 13, 2020
"""

import introcs

rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}


def is_roman(rom):
    """
    Returns True if the given value on rom is a Roman Numeral.

    Example: is_roman('XIX') returns True
    Example: is_roman(23) returns False
    Example: is_roman('iefj') returns False

    :param rom: a string to check
    precondition: rom is a string with a valid roman numeral
    :return: type is bool
    """
    # verify that rom is a string
    # verify that rom has valid roman numerals
    b = None

    for i in rom:
        if i in rom_num.keys():
            b = True
            # print('llego')
        else:
            b = False
            # print('aca')

    return b


def convert(rom):
    """
    Returns the given roman numeral value in natural numeral value.

    Example: convert('V') returns 5
    Example: convert('XX') returns 20
    Example: convert('CLIV') returns 154

    :param rom: a string to convert
    precondition: rom is a string with roman numerals
    :return: a str
    """
    # verify if rom is a valid roman number

    # take each index in rom and convert it individually to natural numbers
    # make the sum and subtraction
    # return the converted number
