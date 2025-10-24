#Write a python program to sort a dictionary by value.
from itertools import product

a = {"a":12,"b":23,"c":6,"d":91,"e":45}
a = sorted(a.values())
print(a)

"""
OUTPUT:-
[6, 12, 23, 45, 91]
"""

# Write a python program to sort a dictionary by key

a1={12:"a",91:"b",6:"c",45:"d",23:"e"}
print(sorted(a1.keys()))

"""
OUTPUT:-
[6, 12, 23, 45, 91]
"""

# Write a python script to print a dictionary
# where the keys are numbers between 1 and 15 and the
# values are square of keys

b = {}
for i in range(1,16):
    b[i] = i**2
print(b)

"""
OUTPUT:-
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
"""

# Write a program to multiply all the items in a dictionary.

c = {"a":1,"b":2,"c":3,"d":4,"e":5}
product=1
for i in c:
    product *= c[i]
print(product)

"""
OUTPUT:-
120
"""
