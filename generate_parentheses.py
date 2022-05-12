# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def dfs(left, right, cur):
            if left > right or left < 0 or right < 0:
                return
            if left == right == 0:
                res.append(cur)

            dfs(left-1, right, cur + "(")
            dfs(left, right - 1, cur + ")")

        dfs(n, n, "")
        return res

# 2


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        cur = []

        def dfs(open, closed):
            if open == closed == n:
                res.append("".join(cur))
                return

            if open < n:
                cur.append("(")
                dfs(open + 1, closed)
                cur.pop()

            if closed < open:
                cur.append(")")
                dfs(open, closed + 1)
                cur.pop()

        dfs(0, 0)
        return res
