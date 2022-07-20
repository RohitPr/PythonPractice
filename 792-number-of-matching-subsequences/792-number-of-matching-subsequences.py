class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        def isSubseq(s1, s2):
            i = j = 0
            
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1
                j += 1
            return len(s1) == i
        
        
        cache = {}
        count = 0
        
        for word in words:
            if word not in cache:
                if isSubseq(word, s):
                    count += 1
                    cache[word] = True
                else:
                    cache[word] = False
            
            else:
                if cache[word]:
                    count += 1
        
        return count