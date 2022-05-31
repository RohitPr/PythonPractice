class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seenSet = set()
        
        for i in range(len(s) - k +1):
            seenSet.add(s[i:i + k])
        
        return len(seenSet) == 2 ** k