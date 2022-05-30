class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
            
            for j in range(i, len(s)):
                if self.isPalin(i, j, s): 
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
            
        dfs(0)
        return res
        
    def isPalin(self, i, j, s):
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1

        return True
            
            