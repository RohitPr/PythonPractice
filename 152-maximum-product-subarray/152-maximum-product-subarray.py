class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        
        for a in nums:
            
            tmp = curMax * a
            curMax = max(a * curMin, a * curMax, a)
            curMin = min(a * curMin, tmp,  a)
            res = max(res, curMax)
        
        return res