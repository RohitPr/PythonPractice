class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
#         res = [nums[0]]
        
#         for a in nums[1:]:
#             res.append((res[-1] + a))
        
#         return res
        
        for a in range(1, len(nums)):
            nums[a] = nums[a] + nums[a-1]
        
        return nums