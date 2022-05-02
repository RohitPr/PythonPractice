# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr


# Example 1:

# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.


class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        res = []
        min = float("infinity")

        arr.sort()

        for a in range(len(arr)-1):
            diff = arr[a + 1] - arr[a]

            if diff < min:
                res.clear()
                min = diff

            if diff == min:
                res.append([arr[a], arr[a + 1]])

        return res
