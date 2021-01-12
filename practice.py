"""
Practice
"""
import math

var = lambda x: x**2

print(var(2))

a_list = [1, 2, 3, 4, 5]

print(list(map(lambda x: x**2, a_list)))

print(list(map(math.sqrt, a_list)))