# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: PersonalizedMessage.py

'''
Personalized greeting
Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:

case                        return
name equals owner	        'Hello boss'
otherwise	                'Hello guest'
'''

# my solution
def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"

# clever solution
greet=lambda n,o:'Hello '+'gbuoessst'[n==o::2]

def greet(name, owner):
    return 'Hello '+['guest','boss'][name==owner]

# test cases
import random
# default test cases
test.assert_equals(greet('Daniel', 'Daniel'), 'Hello boss')
test.assert_equals(greet('Greg', 'Daniel'), 'Hello guest')
# extra tests
for i in range(5):
    first='Joe'
    last='Bob'
    test.assert_equals(greet(first, first), 'Hello boss') if random.randint(0,1) == 0 else test.assert_equals(greet(first, last), 'Hello guest')