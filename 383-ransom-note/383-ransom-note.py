class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # rn = collections.Counter(ransomNote)
        # mg = collections.Counter(magazine)
        
        rn, mg = {}, {}
        
        for a in ransomNote:
            rn[a] = 1 + rn.get(a, 0)              
        
        for b in magazine:
            mg[b] = 1 + mg.get(b, 0)
        
        for k, v in rn.items():
            if k not in mg or mg[k] < v:
                return False
        
        return True