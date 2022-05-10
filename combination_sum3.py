# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.


# Example 1:

# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.

class Solution:
    def combinationSum3(self, k, n):
        ret = []

        def dfs(nums, k, n, path):
            if k < 0 or n < 0:
                return
            if k == 0 and n == 0:
                ret.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]])

        dfs(list(range(1, 10)), k, n, [])
        return ret
