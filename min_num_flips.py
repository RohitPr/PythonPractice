# You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

# Type-1: Remove the character at the start of the string s and append it to the end of the string.
# Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
# Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

# The string is called alternating if no two adjacent characters are equal.

# For example, the strings "010" and "1010" are alternating, while the string "0100" is not.


# Example 1:

# Input: s = "111000"
# Output: 2
# Explanation: Use the first operation two times to make s = "100011".
# Then, use the second operation on the third and sixth elements to make s = "101010".

# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        alt1, alt2 = "01"*n, "10"*n

#         for a in range(len(s)):
#             alt1 += "0" if a%2 == 0 else "1"
#             alt2 += "1" if a%2 == 0 else "0"

        l = 0
        res = float("infinity")
        diff1, diff2 = 0, 0

        for a in range(len(s)):

            if s[a] != alt1[a]:
                diff1 += 1

            if s[a] != alt2[a]:
                diff2 += 1

            if (a-l + 1) > n:
                if s[l] != alt1[l]:
                    diff1 -= 1
                if s[l] != alt2[l]:
                    diff2 -= 1
                l += 1

            if (a-l + 1) == n:
                res = min(res, diff1, diff2)

        return res
