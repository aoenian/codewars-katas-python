# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: SetAlarm.py

'''
Write a function named setAlarm which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.

The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:

setAlarm(true, true) -> false setAlarm(false, true) -> false setAlarm(false, false) -> false setAlarm(true, false) -> true

setalarm(true, true) -> false
setalarm(false, true) -> false
setalarm(false, false) -> false
setalarm(true, false) -> true
'''

# my solution
def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    else:
        return False
    
# best practice
def set_alarm(employed, vacation):
    return employed and not vacation
