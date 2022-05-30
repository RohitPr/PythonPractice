class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, s = [], -float("inf")
        
        for n in nums[::-1]:
            if n < s:
                return True
            while stack and stack[-1] < n: 
                s = stack.pop()
            stack.append(n)
        
        return False