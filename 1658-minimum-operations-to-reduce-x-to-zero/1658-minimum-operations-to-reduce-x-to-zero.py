class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        toFind = sum(nums) - x
        
        l = 0
        res = -1
        
        if toFind < 0:
            return -1
        
        for r in range(len(nums)):
            toFind -= nums[r]
            while toFind < 0:
                toFind += nums[l]
                l += 1
            
            if toFind == 0:
                res = max(res, r-l +1)
        
        return (len(nums) - res) if res != -1 else -1