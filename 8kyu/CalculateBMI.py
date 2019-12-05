# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: CalculateBMI.py

'''
Description:
Write function bmi that calculates body mass index (bmi = weight / height ^ 2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
'''

# my solution
def bmi(weight, height):
    bmi = weight / height ** 2
    res = ''
    if bmi <= 18.5:
        res = 'Underweight'
    elif bmi <= 25.0:
        res = 'Normal'
    elif bmi <= 30.0:
        res = 'Overweight'
    else:
        res = 'Obese'
    return res

# best solution
def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]