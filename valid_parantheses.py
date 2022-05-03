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

# Another Version

# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true


def valid_parentheses(string):
    count = []

    for a in string:
        if a == ")":
            if count and count[-1] == "(":
                count.pop()
            else:
                return False
        elif a == '(' or a == ')':
            count.append(a)

    if count:
        return False
    else:
        return True
