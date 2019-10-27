# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: GrasshopperSummation.py

'''
Summation
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

For example:

summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
'''

# my solution
def summation(num):
    return sum(range(num + 1))

# best practice
def summation(num):
    return sum(xrange(num + 1))

# test cases
@test.describe('Basic tests')
def basic_tssts():
    test.assert_equals(summation(1), 1)
    test.assert_equals(summation(8), 36)
    test.assert_equals(summation(22), 253)
    test.assert_equals(summation(100), 5050)
    test.assert_equals(summation(213), 22791)

@test.describe('Random tests')
def random_tests():
    from random import randint
    
    solution = lambda num: num * (num + 1) / 2
    
    for i in range(100):
        rand = randint(1, 500)
        test.assert_equals(summation(rand), solution(rand))