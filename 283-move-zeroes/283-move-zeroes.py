class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for a in range(len(nums)):
            if nums[a] != 0:
                nums[l], nums[a] = nums[a], nums[l]
                l += 1
        
        # for b in range(l,len(nums)):
        #     nums[b] = 0
        