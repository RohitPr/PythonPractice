class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posD = set()
        negD = set()
        
        res = 0
        
        def back(r):
            if r == n:
                nonlocal res
                res += 1
                return
            
            for c in range(n):
                if c in col or (r + c) in posD or (r-c) in negD:
                    continue
                
                col.add(c)
                posD.add(r + c)
                negD.add(r - c)
                back(r + 1)
                col.remove(c)
                posD.remove(r + c)
                negD.remove(r - c)
        
        back(0)
        return res
             