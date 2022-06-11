class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        toFind = sum(nums) - x
        N = len(nums)
        l = 0
        res = -1
        
        if toFind < 0:
            return -1
        
        for r in range(N):
            toFind -= nums[r]
            while toFind < 0:
                toFind += nums[l]
                l += 1
            
            if toFind == 0:
                res = max(res, r-l +1)
        
        return (N - res) if res != -1 else -1