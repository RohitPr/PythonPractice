class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        l, r = 0, k
        res = 0
        strnum = str(num)
        while r <= len(strnum):
            n = int(strnum[l:r])
            
            if not n:
                l += 1
                r += 1
                continue
            
            if num % n == 0:
                res += 1
                
            l += 1
            r += 1
        
        return res