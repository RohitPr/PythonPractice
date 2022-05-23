class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max, count = 0, 0
        
        for a in nums:
            
            if count == 0:
                max = a
            
            if a == max:
                count += 1
            else:
                count -= 1
        
        return max
            