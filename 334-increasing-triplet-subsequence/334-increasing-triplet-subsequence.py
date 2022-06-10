class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        minF = minS = float("inf")
        
        for num in nums:
            if num <= minF:
                minF = num
            elif num <= minS:
                minS = num
            else:
                return True
        return False