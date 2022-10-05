class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        lenS = len(columnTitle)
        n2 = 0
        for i in range(0,lenS):
            n1 = ord(columnTitle[i])-64
            n2 = 26*n2 + n1
        return n2