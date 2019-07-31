# python 3.7
# by Gabriel Martinez

# This program intend to convert romans numbers to decimal number and reverse.


roman_num = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}


def mix_num(nums):
    nums.split()


def convert():
    print("Give me a roman number to convert it to a cardinal number.")
    a = input()
    while True:
        if a in roman_num.keys():
            for z in roman_num.keys():
                if a == z:
                    b = roman_num.get(z)
                    # The remaining code should go here... mix_num()
                    print(b)
            break
        else:
            print("Enter a roman number.")
            a = input()


# The next code also works, but I will keep the first one.
"""for key, value in roman_num.items():
    if a in key:
        print(value)"""

convert()
