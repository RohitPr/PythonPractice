class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         sLen, tLen = [], []
        
#         for a in range(len(s)):
#             sLen.append(s.count(s[a]))
#             tLen.append(t.count(t[a]))
        
#         return(sLen == tLen)
          
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))