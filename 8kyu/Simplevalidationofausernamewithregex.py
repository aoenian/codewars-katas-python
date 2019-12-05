# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: Simplevalidationofausernamewithregex.py

'''
Write a simple regex to validate a username. Allowed characters are:

lowercase letters,
numbers,
underscore
Length should be between 4 and 16 characters (both included).
'''

# my solution
import string
def validate_usr(username):
    #your code here
    isUser = False
    if len(username) < 4 or len(username) > 16 or username.isdigit():
        return isUser
    valid_char = string.ascii_lowercase + string.digits + '_'
    for i in username:
        if i not in valid_char:
            return isUser
    return True

https://tool.oschina.net/uploads/apidocs/jquery/regexp.html

# best practice
import re
def validate_usr(un):
    return re.match('^[a-z0-9_]{4,16}$', un) != None

# test cases
Test.describe("Basic tests")
Test.assert_equals(validate_usr('asddsa'), True)
Test.assert_equals(validate_usr('a'), False)
Test.assert_equals(validate_usr('Hass'), False)
Test.assert_equals(validate_usr('Hasd_12assssssasasasasasaasasasasas'), False)
Test.assert_equals(validate_usr(''), False)
Test.assert_equals(validate_usr('____'), True)
Test.assert_equals(validate_usr('012'), False)
Test.assert_equals(validate_usr('p1pp1'), True)
Test.assert_equals(validate_usr('asd43 34'), False)
Test.assert_equals(validate_usr('asd43_34'), True)

Test.describe("Random tests")
from random import randint
validate_sol=lambda u: len(u)>3 and len(u)<17 and all(x in "0123456789_abcdefghijklmnopqrstuvwxyz" for x in u)
base="0123456789_abcdefghijklmnopqrstuvwxyz"
wrong=" ,.'?!ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for _ in range(40):
  user="".join([base[randint(0,len(base)-1)] if randint(0,10)<10 else wrong[randint(0,len(wrong)-1)] for qu in range(randint(3,17))])
  Test.it("Testing for "+repr(user))
  Test.assert_equals(validate_usr(user),validate_sol(user),"It should work for random inputs too")