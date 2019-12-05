# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: Drawstairs.py

"""
given a number n, draw stairs with 'I' n tall and n wide, with the tallest in the top left. Example (with - to represent spaces; DO NOT USE THEM IN THE SOLUTIONS! USE SPACES IN SOLUTION! the "-"s are for clarity.): draw_stairs(3) == '''I\n_I\n__I'''

For example, a 7-step stairs should be drawn like this:

const sevenStepStairs = drawStairs(7);
I
 I
  I
   I
    I
     I
      I
"""

# my solution
def draw_stairs(n):
    # do something
    stairs = ''
    for i in range(n):
        stairs = stairs + ' '*i + 'I' + '\n'
    return stairs.strip('\n')

# best practice
def draw_stairs(n):
    return '\n'.join(' '*i+'I' for i in range(n))

# test cases
Test.it("Fixed Tests")
stairs = '''I\n I\n  I'''
test.assert_equals(draw_stairs(3), stairs)
stairs = '''I\n I\n  I\n   I\n    I'''
test.assert_equals(draw_stairs(5), stairs)
Test.it("30 Random Tests")
def draw(n):
    stairs = ''
    for x in range(n):
        stairs += ' '*x + 'I' + '\n'
    return stairs.rstrip('\n')
from random import randint as r
for x in range(30):
    num = r(1, 100)
    test.assert_equals(draw_stairs(num), draw(num))