class Solution:  
    
    def strCheck(self, s):
        t = ''
        l = 0
        
        for a in range(len(s)):
            if s[a] != "#": 
                t += s[a]
                l += 1
                
            if s[a] == "#":
                if t:
                    t = t[0:l-1]
                    l -= 1
        
        return t
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        return (self.strCheck(s) == self.strCheck(t)) 
        