class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         res = len(nums)
        
#         for a in range(len(nums)):
#             res += (a - nums[a])
        
#         return res
    
        res = len(nums)
        for a in nums:
            res ^= a

        for a in range(len(nums)):
            res ^= a

        return res