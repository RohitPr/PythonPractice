class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res, stack = 0, [-1]
        
        for i, v in enumerate(s):
            if v == ')':
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                    continue
            stack.append(i)
        
        return res