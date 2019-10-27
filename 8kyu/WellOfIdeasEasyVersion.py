# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: WellOfIdeasEasyVersion.py

'''
For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 
'good' and bad ideas 'bad'. If there are one or two good ideas, 
return 'Publish!', if there are more than 2 return 'I smell a series!'. 
If there are no good ideas, as is often the case, return 'Fail!'.
'''

# my solution
def well(x):
    count = 0
    res = ''
    for i in x:
        if i == 'good':
            count += 1
    if count > 2:
        res = 'I smell a series!'
    elif count == 0:
        res = 'Fail!'
    else:
        res = 'Publish!'
    return res

# best practice
def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'

# test cases
test.describe("Example Cases")

test.assert_equals(well(['bad', 'bad', 'bad']), 'Fail!')
test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!')

test.describe("Random Tests")

from random import randint, choice

def well_random_tests(x):
    count_ = x.count('good')
    if count_ == 0: return 'Fail!'
    if count_ <= 2: return 'Publish!'
    elif count_ > 2: return 'I smell a series!'

names=['good', 'bad', 'bad', 'bad', 'bad', 'bad']
for i in range(100):
    x=[]; len_ = randint(0,15)
    for k in range(len_ + 1):
        name = choice(names)
        x.append(name)
    result = well_random_tests(x)
    res = well(x)
    test.it("Testing for " + str(x))
    test.assert_equals(res, result)