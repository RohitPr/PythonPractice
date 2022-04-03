# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

from math import sqrt


def find_next_square(sq):
    num = sqrt(sq)
    if num.is_integer():
        return((num+1)**2)
    else:
        return -1
