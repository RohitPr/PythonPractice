class Solution:
    def checkValidString(self, s: str) -> bool:
        left, right = 0, 0
        
        for a in s:
            if a == '(':
                left, right = left + 1, right + 1
            elif a == ')':
                left, right = left - 1, right - 1
            else:
                left, right = left - 1, right + 1
            
            if right < 0:
                return False
            
            if left < 0:
                left = 0
            
        return left == 0
                