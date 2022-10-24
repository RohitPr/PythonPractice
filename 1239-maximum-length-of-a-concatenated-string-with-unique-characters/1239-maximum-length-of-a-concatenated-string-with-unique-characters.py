class Solution:
    def maxLength(self, arr: List[str]) -> int:
        wordList = [""]
        res = 0
        
        for word in arr:
            for a in wordList:
                tmpWord = a + word
                if len(tmpWord) != len(set(tmpWord)):
                    continue
                wordList.append(tmpWord)
                res = max(res, len(tmpWord))
        
        return res
                