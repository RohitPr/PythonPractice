# https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, ops: list[str]) -> int:
        stack = []

        for a in ops:
            if a == 'C':
                stack.pop()
            elif a == 'D':
                stack.append(2 * stack[-1])
            elif a == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(a))

        return sum(stack)
