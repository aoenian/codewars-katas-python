# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: MessiGoalsFunction.py

"""
Description:
Messi goals function
Messi is a soccer player with goals in three leagues:

LaLiga
Copa del Rey
Champions
Complete the function to return his total number of goals in all three leagues.

Note: the input will always be valid.

For example:

5, 10, 2  -->  17
"""

# my solution
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga+copaDelRey+championsLeague

# Best Practices
def goals(*a):
    return sum(a)

# Test Cases:
Test.describe('Random tests')
from random import randint

for i in range(50):
    l = randint(0, 50)
    c = randint(0, 20)
    r = randint(0, 10)
    Test.assert_equals(goals(l, c, r), l + c + r)