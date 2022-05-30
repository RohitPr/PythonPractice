class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = [0] * 26
        
        for a in s:
            res[ord(a) - ord('a')] += 1
 
        for a in range(len(s)):
            if res[ord(s[a]) - ord('a')] == 1:
                return a
        
        return -1
        