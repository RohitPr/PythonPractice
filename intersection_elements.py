# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.


# Example 1:

# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2]


# 1
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = set()
        for a in nums1:
            if a in nums2 and a not in res:
                res.add(a)

        return(list(res))

# 2


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        numS1 = set(nums1)
        numS2 = set(nums2)

        return(list(numS1 & numS2))
