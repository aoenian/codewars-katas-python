# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: CenturyFromYear.py

'''
Introduction
The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.

Task :
Given a year, return the century it is in.

Input , Output Examples ::
centuryFromYear(1705)  returns (18)
centuryFromYear(1900)  returns (19)
centuryFromYear(1601)  returns (17)
centuryFromYear(2000)  returns (20)
Hope you enjoy it .. Awaiting for Best Practice Codes

Enjoy Learning !!!
'''

# my solution
def century(year):
    if 1<=year<=100:
        return 1
    else:
        quotient, remainder = divmod(year, 100)
        if remainder == 0:
            return quotient
        else:
            return quotient + 1
        
# best practice
def century(year):
    return (year + 99) // 100

def century(year):
    return (year - 1) // 100 + 1

import math
def century(year):
    return math.ceil(year / 100)

# test cases
test.describe('Basic Tests')

test.it('Sample Cases')
test.assert_equals(century(1705), 18, 'Testing for year 1705')
test.assert_equals(century(1900), 19, 'Testing for year 1900')
test.assert_equals(century(1601), 17, 'Testing for year 1601')
test.assert_equals(century(2000), 20, 'Testing for year 2000')
test.assert_equals(century(356), 4, 'Testing for year 356')
test.assert_equals(century(89), 1, 'Testing for year 89')


import random
test.it('Random Tests')
def rand_tests():
    
    g_c = lambda y: (y + 99) // 100

    for i in range(100):
        year = random.randint(1, 1000000)
        test.assert_equals(century(year), g_c(year), 'Testing for year {}'.format(year))


rand_tests()