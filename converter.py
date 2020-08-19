"""
A simple program that convert roman numerals to natural numbers and vice versa.

This module in intended to run as a script.

Author: Gabriel Martinez
Date: August 13, 2020
"""

import roman_functions

ask = input('Give me a roman numeral: ')

y = roman_functions.conversion(ask)

print(ask + ' in natural number is ' + str(y) + '.')
