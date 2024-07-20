"""
Just a simple test of the tqdm package.

Author: Gabriel Martinez
Date: July 20, 2024
"""

from tqdm import tqdm
"""
Based on official documentation:

Decorate an iterable object, returning an iterator which acts exactly
like the original iterable, but prints a dynamically updating
progressbar every time a value is requested.
"""

for i in tqdm(range(10000000)):
    "range(million)"
    ...

print("done!")
