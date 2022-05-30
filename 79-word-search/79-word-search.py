class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROW, COL = len(board), len(board[0])
        visit = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if(r >= ROW or c >= COL or r < 0 or c < 0 or (r, c) in visit or board[r][c] != word[i]):
                return False
             
            visit.add((r, c))
            
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            visit.remove((r,c))
            return res
            
        for a in range(ROW):
            for b in range(COL):
                if dfs(a, b, 0): return True
        
        return False