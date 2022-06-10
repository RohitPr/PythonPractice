class Solution:
    """
    @param nums: A list of integers
    @return: nothing
    """

    def wiggle_sort(self, nums: list[int]):
        # write your code here

        for a in range(1, len(nums)):
            if (a % 2 == 1 and nums[a] < nums[a-1]) or (a % 2 == 0 and nums[a] > nums[a-1]):
                nums[a], nums[a-1] = nums[a-1], nums[a]

        return nums
