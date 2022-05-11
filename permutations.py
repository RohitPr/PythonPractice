# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:

# Input: nums = [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, cur):
            if not nums:
                res.append(cur.copy())

            for a in range(len(nums)):
                dfs(nums[a+1:] + nums[:a], cur + [nums[a]])

        dfs(nums, [])
        return res
