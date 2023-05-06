# -*- coding: utf-8 -*-
"""Python Assignments

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P3EeJ1sR-xvyfChq1sK4o0wDn_eEBWfE

##Python Assignments

1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

empList = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        empList.append(i)

print(empList, sep=',')

"""2. Write a python program tto accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name."""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
reversed_name = full_name[::-1]
print(reversed_name)

"""3. Write a Python program to find the volume of a sphere with diameter 12 cm."""

import math

dia = 12
rad = dia / 2
vol = (4/3) * math.pi * (rad ** 3)

print("The volume of the sphere is:", vol, "cubic cm")

