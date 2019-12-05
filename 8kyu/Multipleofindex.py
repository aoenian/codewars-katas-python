# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: Multipleofindex.py

'''
Return a new array consisting of elements which are multiple of their own index in input array (length > 1).

Some cases:

[22, -6, 32, 82, 9, 25] =>  [-6, 32, 25]

[68, -1, 1, -7, 10, 10] => [-1, 10]

[-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68] => [-85, 72, 0, 68]
'''

# my solution
def multiple_of_index(arr):
    new_arr = []
    j = 0
    for i in arr:
        if i == 0 and j == 0:
            new_arr.append(i)
            j+=1
            continue
        elif j==0:
            j+=1
            continue
        elif i%j == 0:
            new_arr.append(i)
        j+=1
    return new_arr

# use range
def multiple_of_index(arr):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] == 0 and i == 0:
            new_arr.append(0)
            continue
        elif i == 0:
            continue
        elif arr[i] % i == 0:
            new_arr.append(arr[i])
    return new_arr

# best practice
# 不过这个程序没有考虑到第一个元素为0的情况

def multiple_of_index(l):
    return [l[i] for i in range(1, len(l)) if l[i] % i == 0]
