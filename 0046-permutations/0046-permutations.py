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