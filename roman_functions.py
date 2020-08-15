"""
A module with a series of functions to convert roman numerals to natural numbers and vice versa.

Author: Gabriel Martinez
Date: August 13, 2020
"""

import introcs

rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}


def is_roman(rom):
    """
    Returns True if the given value on rom is a Roman Numeral.

    Example: is_roman('XIX') returns True
    Example: is_roman(23) returns False
    Example: is_roman('iefj') returns False

    :param rom: a string to check
    precondition: rom is a string
    :return: type is bool
    """
    assert type(rom) == str

    b = None

    for i in rom:
        if i in rom_dict.keys():
            b = True
            # print('llego')
        else:
            b = False
            # print('aca')

    return b


def rom_to_nat(rom):
    """
    Return a list of translated rom to individual natural numbers.

    Example: rom_to_nat('VII') return nat_list = ['5', '1', '1']

    :param rom: a string to convert
    precondition: rom is a string with a valid roman number
    :return: a list of integer(s)
    """
    # verify if rom is a valid roman number
    # assert is_roman(rom)

    rom_list = list(rom)
    # print(rom_list)
    nat_list = list()
    # print(nat_list)

    for a in rom_list:
        # a is each value in the list rom_list
        # take each index in rom_list and convert it individually to natural numbers
        for b in rom_dict.keys():
            # b are each key in the dictionary
            if a == b:
                c = rom_dict[b]
                # c represents the value of the key b in rom_dict
                # print(c)
                nat_list.append(c)
                # print(nat_list)
    return nat_list


def conversion(rom):
    """
    Returns the given roman numeral value in natural numeral value.

    Example: convert('V') returns 5
    Example: convert('XX') returns 20
    Example: convert('CLIV') returns 154

    :param rom: a string to convert
    precondition: rom is a string with valid roman numerals
    :return: a int
    """
    nat_list = rom_to_nat(rom)
    # print(nat_list)
    result = int

    print('new for loop')
    for x in nat_list:
        print(x)
        if nat_list.index(x) < len(nat_list) - 1:
            print('yep' + str(len(nat_list) - 1))
            prox = nat_list.index(x) + 1
            print('jan' + str(prox))
            y = nat_list[prox]
            print('this' + str(y))

        if x >= y:
            result = x + y
            print('pues' + str(result))

        else:
            print('aqui')

    # make the sum and subtraction
    return result


print(conversion('XV'))
