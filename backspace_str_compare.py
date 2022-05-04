# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.


# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

class Solution:
    def strCheck(self, st):
        res = []
        st = list(st)

        for i in st:
            if i == '#':
                if res:
                    res.pop()
            else:
                res.append(i)

        return ''.join(res)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return (self.strCheck(s) == self.strCheck(t))


# O(n) Runtime, O(1) Space

class Solution:

    def strCheck(self, s):
        t = ''
        l = 0

        for a in range(len(s)):
            if s[a] != "#":
                t += s[a]
                l += 1

            if s[a] == "#":
                if t:
                    t = t[0:l-1]
                    l -= 1

        return t

    def backspaceCompare(self, s: str, t: str) -> bool:
        return (self.strCheck(s) == self.strCheck(t))
