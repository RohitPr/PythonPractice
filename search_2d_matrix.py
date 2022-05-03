# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        top, bot = 0, ROW-1

        while top <= bot:
            mid = (top + bot)//2

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break

        if not(top <= bot):
            return False

        row = (top + bot) // 2
        l, r = 0, COL - 1

        while l <= r:

            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                r = mid - 1

        return False
