# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: AlphabeticalAddition.py

'''
Description:
Your task is to add up letters to one letter.

The function will be given a variable amount of arguments, each one being a letter to add.

Notes:
Letters will always be lowercase.
Letters can overflow (see second to last example of the description)
If no letters are given, the function should return 'z'
Examples:
add_letters('a', 'b', 'c') = 'f'
add_letters('a', 'b') = 'c'
add_letters('z') = 'z'
add_letters('z', 'a') = 'a'
add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
add_letters() = 'z'

Confused? 
Start by converting the letters to numbers, a => 1, b => 2, etc. Add them up. 
Think about the overflow yourself. Once that's done, convert it back to a letter.
'''


# my solution
def add_letters(*letters):
    sum = 0
    for c in letters:
        sum = ord(c) + sum
    sum = (sum - len(letters)*96) % 26
    return 'z' if sum==0 else chr(sum+96)

# best practice
def add_letters(*letters):
    return chr( (sum(ord(c)-96 for c in letters)-1)%26 + 97)

# test cases
from random import randint
from functools import reduce

@test.describe("Fixed tests")
def fixed_tests():
    tests = [
        (['a', 'b', 'c'], 'f'),
        (['z'], 'z'),
        (['a', 'b'], 'c'),
        (['c'], 'c'),
        (['z', 'a'], 'a'),
        (['y', 'c', 'b'], 'd'),
        ([], 'z')
    ]
    for i, o in tests:
        str = ', '.join(['"' + s + '"' for s in i])
        @test.it("add_letters(" + str + ")")
        def fixed_test():
            Test.assert_equals(add_letters(*i), o)

@test.describe("Random tests")
def random_tests():
    sol = lambda *letters: 'z' if len(letters) == 0 else reduce(lambda x, _: 'a' if x == 'z' else chr(ord(x) + 1), range(reduce(lambda acc, item: acc + (ord(item) - 96), letters, -1)), 'a')
    for t in range(100):
        arr = [chr(randint(97, 122)) for i in range(randint(1, 10))]
        str = ', '.join(['"' + s + '"' for s in arr])
        @test.it("add_letters(" + str + ")")
        def random_test():
            Test.assert_equals(add_letters(*arr), sol(*arr))