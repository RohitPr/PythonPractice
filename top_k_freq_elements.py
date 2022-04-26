# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


# Example 1:

# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        for key, value in count.items():
            freq[value].append(key)

        res = []

        for a in range(len(freq)-1, 0, -1):
            for i in freq[a]:
                res.append(i)
                if len(res) == k:
                    return res
