# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: InviteMoreWomen.py

'''
Description:
Task
King Arthur and his knights are having a New Years party. Last year Lancelot was jealous of Arthur, because Arthur had a date and Lancelot did not, and they started a duel.

To prevent this from happening again, Arthur wants to make sure that there are at least as many women as men at this year's party. He gave you a list of integers of all the party goers.

Arthur needs you to return true if he needs to invite more women or false if he is all set.

Input/Output
[input] integer array L ($a in PHP)

An array (guaranteed non-associative in PHP) representing the genders of the attendees, where -1 represents women and 1 represents men.

2 <= L.length <= 50

[output] a boolean value

true if Arthur need to invite more women, false otherwise.
'''

# my solution
def invite_more_women(arr):
    men = arr.count(1)
    women = arr.count(-1)
    return True if men>women else False

# Best Practices
def invite_more_women(arr):
    return sum(arr) > 0

def invite_more_women(arr):
    return arr.count(1) > arr.count(-1)

# test cases
Test.describe("Basic Tests")
Test.assert_equals(invite_more_women([1, -1, 1]),True)
Test.assert_equals(invite_more_women([-1, -1, -1]),False)
Test.assert_equals(invite_more_women([1, -1]),False)
Test.assert_equals(invite_more_women([1, 1, 1]),True)
Test.assert_equals(invite_more_women([]),False)

Test.describe("Random Tests")
from random import randint
sol=lambda arr: sum(arr)>0

for _ in range(40):
  arr=[-1**randint(0,1) for q in range(randint(1,35))]
  Test.it("Testing for "+str(arr))
  Test.assert_equals(invite_more_women(arr),sol(arr),"It should work for random inputs too")