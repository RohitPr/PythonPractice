class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for a in range(len(s)):
            # Odd Lenght Substrings
            l = r = a
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # Even Length Substring
            l, r = a, a+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
        return res