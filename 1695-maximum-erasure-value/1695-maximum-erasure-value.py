class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        seen = set()
        res, cur_sum = 0, 0
        
        
        for r in range(len(nums)):
            while nums[r] in seen:
                cur_sum -= nums[l]
                seen.remove(nums[l])
                l += 1
            
            cur_sum += nums[r]
            seen.add(nums[r])
            res = max(res, cur_sum)
        
        return res
                