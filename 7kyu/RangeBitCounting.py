# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: RangeBitCounting.py

'''
Description:
Task
You are given two numbers a and b where 0 ≤ a ≤ b. Imagine you construct an array of all the integers from a to b inclusive. You need to count the number of 1s in the binary representations of all the numbers in the array.

Example
For a = 2 and b = 7, the output should be 11

Given a = 2 and b = 7 the array is: [2, 3, 4, 5, 6, 7]. Converting the numbers to binary, we get [10, 11, 100, 101, 110, 111], which contains 1 + 2 + 1 + 2 + 2 + 3 = 11 1s.

Input/Output
[input] integer a

Constraints: 0 ≤ a ≤ b.

[input] integer b

Constraints: a ≤ b ≤ 100.

[output] an integer
'''

# my solutions
def range_bit_count(a, b):
    count = 0
    for n in range(a, b+1):
        while n > 0:
            remainder = n % 2
            if remainder:
                count+=1
            n //= 2
    return count

# best practices
def range_bit_count(a, b):
    return sum(bin(i).count('1') for i in range(a, b+1))

# test cases
Test.it("Basic Tests")
Test.assert_equals(range_bit_count(2,7) , 11)
Test.assert_equals(range_bit_count(0,1) , 1)
Test.assert_equals(range_bit_count(4,4) , 1)


#random tests part
from random import randint
import math
def an(a, b):
  r=0
  for i in range(a,b+1): r+=len(bin(i).split('1'))-1
  return r

def rand(a, b):
  return randint(a, b)
#Test.describe("100 Random Tests")
Test.it("100 Random Tests")
for _ in range(100):
  r1=rand(0,30)
  r2=r1+rand(0,70)
  ans=an(r1,r2)
  
  print("</b><font color='#00cc00'>Testing for:\n</font><font color='cccc00'>"
  +("a = %s" %(r1))
  +("\nb = %s" %(r2))
  #+("\nvalue2 = %s" %(r3))
  #+("\nweight2 = %s" %(r4))
  #+("\nmax_w = %s" %(r5))
  +("\ncorrect result should be %s" %(ans))
  +"</font></b>")  
  
  Test.assert_equals(range_bit_count(r1,r2),ans,"Your result is")

