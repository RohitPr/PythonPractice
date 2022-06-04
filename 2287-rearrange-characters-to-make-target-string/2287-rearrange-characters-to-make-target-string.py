class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        countS, countT = {}, {}
        res = float("inf")
        
        for a in s:
            countS[a] = 1 + countS.get(a, 0)
            
        for b in target:
            countT[b] = 1 + countT.get(b, 0)
        
        for t in countT:
            if t not in countS or countS[t] < countT[t]:
                return 0
            
            res = min(res, countS[t]//countT[t])
                
        
        return res