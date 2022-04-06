# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


# Example 1:

# Input: s = "()"
# Output: true

# Input: s = "(]"
# Output: false


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpen = {")": "(",
                     "]": "[",
                     "}": "{"
                     }

        for a in s:
            if a in closeOpen:
                if stack and stack[-1] == closeOpen[a]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(a)

        if stack:
            return False
        else:
            return True
