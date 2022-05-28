class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        
        for a in nums:
            if a in seen:
                return a
            seen.add(a)
        return -1