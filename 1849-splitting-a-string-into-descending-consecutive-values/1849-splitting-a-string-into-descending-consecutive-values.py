class Solution:
    def splitString(self, s: str) -> bool:
        
        def dfs(index, prev):
            if index == len(s):
                return True
            for j in range(index,len(s)):
                val = int(s[index: j + 1])
                if val + 1 == prev and dfs(j + 1, val):
                    return True    
            return False
                
        
        for a in range(len(s) - 1):
            val = int(s[:a + 1])
            if dfs(a + 1, val):
                return True
            
        return False
        
        