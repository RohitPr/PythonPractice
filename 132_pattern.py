# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.

# Example 1:

# Input: nums = [1, 2, 3, 4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.


class Solution:
    def find132pattern(self, nums) -> bool:
        stack, s3 = [], -float("inf")
        for n in nums[::-1]:
            if n < s3:
                return True
            while stack and stack[-1] < n:
                s3 = stack.pop()
            stack.append(n)
        return False


# s = Solution()

# print(s.find132pattern([1, 2, 3, 5, 7, 8, 9]))
