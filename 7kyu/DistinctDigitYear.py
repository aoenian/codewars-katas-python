# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: DistinctDigitYear.py

'''
Task
The year of 2013 is the first year after the old 1987 with only distinct digits.

Now your task is to solve the following problem: given a year number, find the minimum year number which is strictly larger than the given one and has only distinct digits.

Input/Output
[input] integer year

1000 ≤ year ≤ 9000

[output] an integer

the minimum year number that is strictly larger than the input number year and all its digits are distinct.
'''

# my solution
def distinct_digit_year(year):
    dis_year = year + 1
    while True:
        length = len(str(dis_year))
        distict_length = len(set(str(dis_year)))
        if length == distict_length:
            return dis_year
        else:
            dis_year += 1
            
# best practice
def distinct_digit_year(year):
    year += 1
    while len(set(str(year))) != 4:
        year += 1
    return year

