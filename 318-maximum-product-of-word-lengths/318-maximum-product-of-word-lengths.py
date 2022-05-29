class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        res = 0
        
        def check(s1, s2):
            for a in s1:
                if a in s2:
                    return False
            
            return True
        
        for i in range(len(words)):
            for j in range(i, len(words)):
                if check(words[i], words[j]):
                    res = max(res, len(words[i] * len(words[j])))
        
        return res