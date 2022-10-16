class Solution:
    def longestPalindrome(self, s: str) -> int:
        numSet = set()
        
        res = 0
        
        for a in s:
            if a in numSet:
                numSet.remove(a)
                res += 2
            else:
                numSet.add(a)
        
        if numSet:
            return (res + 1)
        else:
            return res