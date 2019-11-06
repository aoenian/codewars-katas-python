# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: Tetrisscoringsystem.py

'''
Description:
A History Lesson
Tetris is a puzzle video game originally designed and programmed by Soviet Russian software engineer Alexey Pajitnov. The first playable version was completed on June 6, 1984. Pajitnov derived its name from combining the Greek numerical prefix tetra- (the falling pieces contain 4 segments) and tennis, Pajitnov's favorite sport.

About scoring system
The scoring formula is built on the idea that more difficult line clears should be awarded more points. For example, a single line clear is worth 40 points, clearing four lines at once (known as a Tetris) is worth 1200.

A level multiplier is also used. The game starts at level 0. The level increases every ten lines you clear. For our task you can use this table:

Level   Points for 1 line   Points for 2 lines  Points for 3 lines	Points for 4 lines
0       40	                100                 300	                1200
1	    80	                200	                600	                2400
2	    120	                300	                900	                3600
3	    160	                400	                1200	            4800
...
7	    320	                800	                2400	            9600
...	    For level n you must determine the formula by yourself using given examples from the table.

Task
Calculate the final score of the game using original Nintendo scoring system

Input
Array with cleaned lines.
Example: [4, 2, 2, 3, 3, 4, 2]
Input will always be valid: array of random length (from 0 to 5000) with numbers from 0 to 4.

Ouput
Calculated final score.
def get_score(arr) -> int: return 0

Example
>>> arr = [4, 2, 2, 3, 3, 4, 2]
>>> get_score(arr)
4900
Step 1: +1200 points for 4 lines (current level 0). Score: 1200;
Step 2: +100 for 2 lines. Score: 1300;
Step 3: +100;
Step 4: +300 for 3 lines (current level still 0).
Total number of cleaned lines 11 (4 + 2 + 2 + 3), so level goes up to 1 (level ups each 10 lines);
Step 5: +600 for 3 lines (current level 1);
Step 6: +2400;
Step 7: +200. Total score: 4900 points.

Other
If you like the idea: leave feedback, and there will be a series of katas with higher difficulty levels on the Tetris theme.
'''

# my solution
def get_score(arr):
    score = 0
    level = 0
    weight = 1
    sum_line = 0
    line_score = [0, 40, 100, 300, 1200]
    for line in arr:
        level = sum_line // 10
        weight = level + 1
        score += line_score[line] * weight
        sum_line += line
    return score

# best practice
points = [0, 40, 100, 300, 1200]

def get_score(arr) -> int:
    cleared = 0
    score = 0
    for lines in arr:
        level = cleared // 10
        score += (level+1) * points[lines]
        cleared += lines
    return score

# test cases
Test.describe("Tetris scoring system")

Test.it("Basic tests")
Test.assert_equals(get_score([0, 1, 2, 3, 4]), 1640)
Test.assert_equals(get_score([0, 1, 1, 3, 0, 2, 1, 2]), 620)
Test.assert_equals(get_score([2, 0, 4, 2, 2, 3, 0, 0, 3, 3]), 3300)

Test.it("Special tests")
Test.assert_equals(get_score([0]), 0)
Test.assert_equals(get_score([]), 0)

from random import randint
generate_arr = lambda n: [randint(0, 4) for x in range(n)]
scoring_table_solution = [0, 40, 100, 300, 1200]
def get_score_solution(arr) -> int:
    score = lines = 0
    for x in arr:
        score += scoring_table_solution[x] * (lines // 10 + 1)
        lines += x
    return score

