class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        def countP(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            return count
        
        for a in range(len(s)):
            # Odd Lenght Substrings
            res += countP(a,a)
            # Even Length Substring
            res += countP(a, a+1)
        
        return res    
            
       
        
        