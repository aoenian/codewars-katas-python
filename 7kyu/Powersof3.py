# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: Powersof3.py

'''
Description:
Given a positive integer N, return the largest integer k such that 3^k < N.

For example,

largestPower(3) = 0
largestPower(4) = 1
You may assume that the input to your function is always a positive integer.
'''

# my solution
def largestPower(n):
    flag = True
    res = -1
    while flag:
        if 3 ** res < n:
            res += 1
        else:
            flag = False
    return res

# best prctice
from math import ceil, log
def largestPower(n):
    return ceil(log(n, 3)) - 1

from math import log
def largestPower(n):
    k = int(log(n, 3))
    return k if 3 ** k < n else k - 1

# test cases
import math, random

def solution(N):
    k = math.log(N, 3)
    if int(k) == k:
        return int(k) - 1
    else:
        return int(k)

Test.it("Small cases")
Test.assert_equals(largestPower(2), 0)
Test.assert_equals(largestPower(3), 0)
Test.assert_equals(largestPower(4), 1)
Test.assert_equals(largestPower(5), 1)
Test.assert_equals(largestPower(7), 1)

Test.it("Large cases")
Test.assert_equals(largestPower(81), 3)
Test.assert_equals(largestPower(82), 4)
Test.assert_equals(largestPower(59049), 9)
Test.assert_equals(largestPower(59050), 10)
Test.assert_equals(largestPower(123456789), 16)
Test.assert_equals(largestPower(987654321), 18)

Test.it("Edge case")
Test.assert_equals(largestPower(1), -1)

Test.it("Random cases")
for _ in range(30):
    N = random.randint(1, 10**20)
    Test.assert_equals(largestPower(N), solution(N), 
        "Test failed on " + str(N))


