# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Input: strs = ["dog","racecar","car"]
# Output: ""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        small = min(strs)
        big = max(strs)
        for i in range(len(small)):
            if small[i] != big[i]:
                return small[:i]
        return small
