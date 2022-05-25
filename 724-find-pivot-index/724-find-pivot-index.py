class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums)
        
        for a in range(len(nums)):

            rightSum -= nums[a]
            
            if leftSum == rightSum:
                return a
            leftSum += nums[a]
            
        return -1