class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resDict = collections.defaultdict(list)
        
        for word in strs:
            alphaList = [0] * 26
            
            for letter in word:
                alphaList[ord(letter) - ord('a')] += 1 
                
            resDict[tuple(alphaList)].append(word)
            
        return resDict.values()