# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.


# Example 1:

# Input: s = "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        res = ""

        for a in s:
            if stack and stack[-1][0] == a:
                stack[-1][1] += 1
            else:
                stack.append([a, 1])

            if stack[-1][1] == 2:
                stack.pop()

        for char, val in stack:
            res += char * val

        return res
