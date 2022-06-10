class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        l = 0
        
        for a in range(len(s)):
            while s[a] in seen:
                seen.remove(s[l])
                l += 1            
            
            res = max(res, a - l + 1 )
            seen.add(s[a])
        
        return res