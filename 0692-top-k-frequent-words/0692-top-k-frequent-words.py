class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = {}
        
        for word in words:
            dict[word] = 1 + dict.get(word,0)
            
        res = sorted(dict, key = lambda x : (-dict[x],x))
        
        return res[:k]