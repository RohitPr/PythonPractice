# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Solution 1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        temp_s = set(s)

        for a in temp_s:
            count_s[a] = s.count(a)
            count_t[a] = t.count(a)

        for k, v in count_s.items():
            if count_s[k] != count_t[k]:
                return False

        return True

# Solution 2(get function sets a default value if the same in not present in the dict/hashmap)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_key = {}
        t_key = {}

        for a in range(len(s)):
            s_key[s[a]] = 1 + s_key.get(s[a], 0)
            t_key[t[a]] = 1 + t_key.get(t[a], 0)

        for k, v in s_key.items():
            if s_key[k] != t_key.get(k, 0):
                return False
        return True

# Solution 3 & 4 (Cheating Solution)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
