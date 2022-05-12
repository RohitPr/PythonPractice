# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def dfs(nums, cur):
            if not nums:
                res.append(cur)

            for a in range(len(nums)):
                if a > 0 and nums[a] == nums[a-1]:
                    continue

                dfs(nums[a+1:] + nums[:a], cur + [nums[a]])

        dfs(nums, [])
        return res
