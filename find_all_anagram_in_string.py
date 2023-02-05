# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        res = []
        listP = [0] * 26
        l = 0

        for a in p:
            listP[ord('a')-ord(a)] += 1

        for b in range(0, len(s)-len(p)+1):
            listS = [0] * 26
            for ch in range(l, l + len(p)):
                listS[ord('a')-ord(s[ch])] += 1
            if listS == listP:
                res.append(l)
            l += 1

        return res
