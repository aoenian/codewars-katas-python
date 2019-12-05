# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: SortandStar.py

'''
You will be given an vector of string(s). You must sort it alphabetically (case-sensitive!!) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.
'''

# my solution
def two_sort(array):
    array.sort()
    value_arr = list(array[0])
    return '***'.join(value_arr)

# best practice
def two_sort(lst):
    return '***'.join(min(lst))

# test cases
import random

@test.describe("Fixed tests")
def fixed_tests():
    Test.assert_equals(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]), 'b***i***t***c***o***i***n' )
    Test.assert_equals(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]), 'a***r***e')
    Test.assert_equals(two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]), 'a***b***o***u***t')
    Test.assert_equals(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]), 'c***o***d***e')
    Test.assert_equals(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]), 'L***e***t***s')

@test.describe("Random Tests")
def random_tests():
    def _solution(a):
        return "***".join(list(sorted(a)[0]))
    
    options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for _ in range(100):
        s = ["".join([random.choice(options) for i in range(random.randint(3, 8))]) for j in range(random.randint(5, 10))]
        Test.assert_equals(two_sort(s[:]), _solution(s))