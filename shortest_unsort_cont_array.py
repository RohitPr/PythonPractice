# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.


# Example 1:

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:

        end = 0
        prev = nums[0]

        for a in range(len(nums)):
            if prev > nums[a]:
                end = a
            else:
                prev = nums[a]

        start = len(nums) - 1
        prev = nums[-1]

        for a in range(len(nums)-1, -1, -1):
            if prev < nums[a]:
                start = a
            else:
                prev = nums[a]

        if end != 0:
            return (end-start + 1)
        else:
            return end
