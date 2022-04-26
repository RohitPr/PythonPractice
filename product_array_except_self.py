# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        prefix = 1
        postfix = 1

        for a in range(len(nums)):
            res[a] = prefix
            prefix *= nums[a]

        for b in range(len(nums)-1, -1, -1):
            res[b] *= postfix
            postfix *= nums[b]

        return res
