#author: MJ
#2020-01-18

import pytest
from magic_squares import Game

"""
TDD:
A number of test cases (commented out by: #) used for developing the functionalities needed
for solving the magis squares exercise.
1. Red phase: implement a failing test
2. 
3. Refactor & unmark the test object

TESTS:
1. num sequence S (of size n*n) is taken as input
2. S is split up into n 'row' sequences s. That is, the first n numbers are popped and put into the first s.
3. S is split up into n 'column' sequences. That is,
    - the nrs at index x, x+n, x+(n*2), ... while n*x < n*n, using x=0 for the first column
4. From S, the diagonals are generated. That is,
    - nrs at index 0, (n*1)+0, (n*2)+1, ... while (n*x)+x <= n*n
    - nrs at index n-1, (n*2)-2, (n*3)-3, ... while n*x <= n*n
5. For each seq, the sums are correctly calculated & compared.
"""

#.....FIXTURES..........#

@pytest.fixture() #Instantiaton
def g():
    game = Game(4)
    return game #the 'g' function is called for each test method

#.....TESTS.............#

def test_all(g):
    #--TDD 1--#
    g.randomNrSeqIsGenerated()
    assert len(g.inputArray) == 16
    #--TDD 2--#
    copyOfInputArray = g.inputArray[:]
    g.sortIntoRows()
    assert len(copyOfInputArray) > 0
    assert len(g.totalArray) == 4
    #--TDD 3--#
    g.sortIntoRows()
    assert len(g.totalArray) == 8
    #--TDD 4--#
    g.sortIntoDiagonals()
    assert len(g.totalArray) == 10
    assert g.totalArray[0][0] == g.totalArray[g.side*2][0]
    #--TDD 5--# 
    if g.sumsAreEqual() == True:
        for i in range(g.size+2):
            assert sum(g.totalArray[i-1]) == sum(g.totalArray[i])
