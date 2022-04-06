# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        count = {}
        for a in range(len(nums)):
            val = target - nums[a]
            if val in count:
                return[count[val], a]
            count[nums[a]] = a

# Return with +1 to the index (Two Sum 2 )


class Solution:
    def twoSum2(self, nums, target):
        num_dict = {}

        for i, v in enumerate(nums):
            val = target - v
            if val in num_dict:
                return(num_dict[val]+1, i+1)
            num_dict[v] = i

# Two Sum 2 with Pointers


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers)-1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return[left+1, right+1]
            elif sum > target:
                right -= 1
            else:
                left += 1
