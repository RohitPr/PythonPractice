# Given an array of strings words(without duplicates), return all the concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.


# Example 1:

# Input: words = ["cat", "cats", "catsdogcats", "dog",
#                 "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
# Output: ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog"
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        wordSet = set(words)

        def dfs(word):

            for a in range(1, len(word)):

                prefix = word[:a]
                suffix = word[a:]

                if ((prefix in wordSet and suffix in wordSet) or (prefix in wordSet and dfs(suffix))):
                    return True

        res = []
        for w in words:
            if dfs(w):
                res.append(w)

        return res
