class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = {0 : 1}
        total = 0
        res = 0
        
        for n in nums:
            total += n
            sub = total - k
            
            res += preSum.get(sub, 0)
            preSum[total] = 1 + preSum.get(total, 0)
            
        return res
            
            