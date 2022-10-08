class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return None
        
        diff=float('inf')
        l, r = 0, len(nums)-1
        res = sum(nums[:3])
        nums.sort()

        for n in range(len(nums)-2):
            n1 = n + 1
            n2 = len(nums) - 1
            
            while n1 < n2:
                numSum = nums[n] + nums[n1] + nums[n2]

                if abs(numSum - target) < diff:
                    diff= abs(numSum - target)
                    res = numSum

                if numSum < target:
                    n1 += 1
                elif numSum > target:
                    n2 -= 1
                else:
                    return target
        
        return res