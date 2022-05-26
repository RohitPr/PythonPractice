class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        
        target = sum(nums) // 2
        
        for a in range(len(nums)):
            cache = set()
            
            for t in dp:
                if t + nums[a] == target:
                    return True
                cache.add(t)
                cache.add(t + nums[a])
                
            dp = cache
        
        return True if target in dp else False