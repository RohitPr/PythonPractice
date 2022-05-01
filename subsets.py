# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

# Include the element
            subset.append(nums[i])
            dfs(i + 1)

# Exclude the element
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
