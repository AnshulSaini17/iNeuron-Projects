# -*- coding: utf-8 -*-
"""Modules , Exception Handling &amp; Database Programming

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P3EeJ1sR-xvyfChq1sK4o0wDn_eEBWfE

##Python Assignments

## Modules , Exception Handling &amp; Database Programming

1. Write a function to compute 5/0 and use try/except to catch the exceptions.
"""

def divide_by_zero():
    try:
        result = 5000/0
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        result = None
    return result

# Example
print(divide_by_zero())

"""2. Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].

 Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
"""

subjects = ["Americans", "Indians"]
verbs = ["play", "watch"]
objects = ["Baseball", "Cricket"]

for subject in subjects:
    for verb in verbs:
        for obj in objects:
            sentence = subject + " " + verb + " " + obj + "."
            print(sentence)
