# -*- coding: utf-8 -*-
"""Dictionaries and Function

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P3EeJ1sR-xvyfChq1sK4o0wDn_eEBWfE

##Python Assignments

##Dictionaries and Function

1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.

 area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

 Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass.
"""

class Triangle:
    def __init__(self):
        self.a = float(input("Enter the first side of triangle: "))
        self.b = float(input("Enter the second side of triangle: "))
        self.c = float(input("Enter the third side of triangle: "))


class Area(Triangle):
    def __init__(self):
        super().__init__()

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return area


t = Area()
print("The area of the triangle is:", t.calculate_area())

"""1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n."""

def filter_long_words(word_list, n):
    filtered_list = []
    for word in word_list:
        if len(word) > n:
            filtered_list.append(word)
    return filtered_list

words = ['anshul', 'loves', 'to', 'do', 'gym']
n = 4

filtered_words = filter_long_words(words, n)
print(filtered_words)

"""2.1 Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words.

Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]

Here 2,3 and 4 are the lengths of the words in the list.
"""

def word_lengths(word_list):
    length = []
    for word in word_list:
        length.append(len(word))
    return length

words = ['anshul', 'loves', 'to', 'do', 'gym']

word_lengths_list = word_lengths(words)
print(word_lengths_list)

"""2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise."""

def is_vowel(char):
    vowels = "aeiouAEIOU"
    if char in vowels:
        return True
    else:
        return False

char1 = 'a'
char2 = 'b'

print(is_vowel(char1))  
print(is_vowel(char2))

