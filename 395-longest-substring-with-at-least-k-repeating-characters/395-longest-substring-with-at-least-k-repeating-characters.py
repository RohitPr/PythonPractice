class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or k > len(s):
            return 0
        
        sCount = {}
        
        for a in s:
            sCount[a] = 1 + sCount.get(a, 0)    
        
        sub1, sub2 = "", ""
        
        for i, v in enumerate(s):
            if sCount[v] < k:
                sub1 = self.longestSubstring(s[i+1:], k)
                sub2 = self.longestSubstring(s[:i], k)
                break
        else:
            return(len(s))
        
        return max(sub1, sub2)
        