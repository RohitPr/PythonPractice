# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        for a in range(len(s1)):
            s1Count[ord(s1[a]) - ord('a')] += 1
            s2Count[ord(s2[a]) - ord('a')] += 1

        matches = 0

        for a in range(26):
            matches += (1 if s1Count[a] == s2Count[a] else 0)

        l = 0

        for a in range(len(s1), len(s2)):
            if matches == 26:
                return True

            right_index = ord(s2[a]) - ord('a')

            s2Count[right_index] += 1

            if s2Count[right_index] == s1Count[right_index]:
                matches += 1
            elif s2Count[right_index] == s1Count[right_index] + 1:
                matches -= 1

            left_index = ord(s2[l]) - ord('a')

            s2Count[left_index] -= 1

            if s2Count[left_index] == s1Count[left_index]:
                matches += 1
            elif s2Count[left_index] == s1Count[left_index] - 1:
                matches -= 1

            l += 1

        return matches == 26
