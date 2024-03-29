# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []

class Solution:
    def letterCombinations(self, digits: str):
        keyMap = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs",
                  '8': "tuv", '9': "wxyz"}

        res = [''] if digits else []

        for n in digits:
            res = [a + q for a in res for q in keyMap[n]]

        return res
