class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = Counter(lt.lower() for lt in licensePlate if lt.isalpha())
        return min((word for word in words if not letters - Counter(word)),key=len)
        