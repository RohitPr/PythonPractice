# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.


# Example 1:

# Input: nums = [3, 1, 2, 4]
# Output: [2, 4, 3, 1]
# Explanation: The outputs[4, 2, 3, 1], [2, 4, 1, 3], and [4, 2, 1, 3] would also be accepted.
# Example 2:

# Input: nums = [0]
# Output: [0]

from collections import deque


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:

        res = sorted(nums, key=lambda x: x % 2 == 0, reverse=True)

        return res

        # nums.sort(key = lambda x: x % 2 == 0, reverse = True)

        # return nums

# 2


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        res = deque()
        l, r = 0, len(nums)-1

        for a in nums:
            if a % 2 == 0:
                res.appendleft(a)
            else:
                res.append(a)
        return res
