"""
A module with a series of functions to convert roman numerals to natural numbers and vice versa.

Author: Gabriel Martinez
Date: August 13, 2020
"""

import introcs

I = 1
i = 'I'

V = 5
v = 'V'

X = 10
x = 'X'

L = 50
l = 'L'

C = 100
c = 'C'


def is_roman(x):
    """
    Returns True if the given value on x is a Roman Numeral.

    Example: is_roman('XIX') returns True
    Example: is_roman(23) returns False
    Example: is_roman('iefj') returns False

    :param x: a string to check
    precondition: x is a string with a valid roman numeral
    :return: type is bool
    """
    # verify that x is a string
    # verify that x has valid roman numerals

    # return bool


def convert(x):
    """
    Returns the given roman numeral value in natural numeral value.

    Example: convert('V') returns 5
    Example: convert('XX') returns 20
    Example:

    :param x: a string to convert
    precondition: x is a string with roman numerals
    :return: a str
    """
    # take each index in x and calculate the number

    # return the converted number
