"""
A test module for roman_functions.py

When run as a script, this module invokes several procedures that test
the various functions in the module roman_functions

Author: Gabriel Martinez
Date: August 13, 2020
"""

import introcs
import roman_functions


def test_is_roman():
    """
    A test for the is_roman function.
    """
    print('Testing is_roman...')

    # Test cases
    result = roman_functions.is_roman('XIX')
    introcs.assert_true(result)

    result = roman_functions.is_roman('CLI')
    introcs.assert_true(result)

    result = roman_functions.is_roman('23')
    introcs.assert_false(result)

    result = roman_functions.is_roman('jqk')
    introcs.assert_false(result)


def test_rom_to_nat():
    """
    A test for the rom_to_nat function.
    """
    print('Testing rom_to_nat...')


def test_conversion():
    """
    A test for conversion.
    """
    print('Testing conversion...')

    # Test cases
    result = roman_functions.conversion('XIX')
    introcs.assert_equals('19', result)


test_is_roman()
test_rom_to_nat()
test_conversion()
print('All test completed successfully.')
