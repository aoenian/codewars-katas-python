# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: FindtheSpeedcuber'stimes.py

'''
Description:
Speedcubing is the hobby involving solving a variety of twisty puzzles, the most famous being the 3x3x3 puzzle or Rubik's Cube, as quickly as possible.

In the majority of Speedcubing competitions, a Cuber solves a scrambled cube 5 times, and their result is found by taking the average of the middle 3 solves (ie. the slowest and fastest times are disregarded, and an average is taken of the remaining times).

In some competitions, the unlikely event of a tie situation is resolved by comparing Cuber's fastest times.

Write a function cube_times(times) that, given an array of floats times returns an array / tuple with the Cuber's result (to 2 decimal places) AND their fastest solve.

For example:

cube_times([9.5, 7.6, 11.4, 10.5, 8.1]) = (9.37, 7.6)
# Because (9.5 + 10.5 + 8.1) / 3 = 9.37 and 7.6 was the fastest solve.
Note: times will always be a valid array of 5 positive floats (representing seconds)
'''

# my solution
def cube_times(times):
    min_time = min(times)
    times.remove(max(times))
    times.remove(min_time)
    sum_time = sum(times)
    res_time = sum_time/3
    return (round(res_time, 2), min_time)

# best practice
def cube_times(times):
    return (round((sum(times) - (min(times) + max(times)))/3 , 2), min(times))

def cube_times(times):
    times = sorted(times)
    return (round(sum(times[1:-1])/3,2), times[0])

# test cases
import numpy as np

@test.describe("cube_times")
def tests():
    @test.it("Basic tests")
    def basic_tests():
        test.assert_equals(cube_times([9.5, 7.6, 11.4, 10.5, 8.1]), (9.37, 7.6))
        test.assert_equals(cube_times([13.4, 12.3, 9.5, 11.9, 20.8]), (12.53, 9.5))
        test.assert_equals(cube_times([28.3, 14.5, 17.3, 8.9, 10.1]), (13.97, 8.9))
    
    @test.it("Random tests")
    def random_tests():
        def validator(times):
            return (round(sum(sorted(times)[1:4]) / 3, 2), min(times))
        
        for i in range(200):
            test_list = [round(x, 2) for x in np.random.uniform(low=5, high=25, size=5)]
            test.assert_equals(cube_times(test_list[:]), validator(test_list))