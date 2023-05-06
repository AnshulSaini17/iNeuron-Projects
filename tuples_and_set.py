# -*- coding: utf-8 -*-
"""Tuples and Set

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P3EeJ1sR-xvyfChq1sK4o0wDn_eEBWfE

##Python Assignments

### Tuples and Set

1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()
"""

def myreduce(function, sequence):
    result = sequence[0]
    for i in sequence[1:]:
        result = function(result, i)
    return result

def sum(x, y):
    return x + y

numbers = [2,3,4,7,3]
print("Sum is:", myreduce(sum, numbers))

def product(x, y):
    return x * y

numbers = [2,3,4,7,0]
print("product is:", myreduce(product, numbers))

"""1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()"""

def myfilter(func, seq):
    result = []
    for i in seq:
        if func(i):
            result.append(i)
    return result

def is_vowel(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return x.lower() in vowels

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print("The vowels are:", myfilter(is_vowel, letters))

"""2. Implement List comprehensions to produce the following lists.

i) ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

ii) ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

iii) [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
[4, 5, 6, 7], [5, 6, 7, 8]]

iv) [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
"""

result = [char * i for char in ['x', 'y', 'z'] for i in range(1, 5)]
print(result)

result_2 = [char * i for i in range(1, 5) for char in ['x', 'y', 'z']]
print(result_2)

result_3 = [[num + i] for num in [2, 3, 4] for i in range(0, 3)]
print(result_3)

result_4 = [(j, i) for i in range(1, 4) for j in range(1, 4)]
print(result_4)
