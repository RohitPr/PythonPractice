class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def back(i,subset):
            if i == len(nums):
                res.append(subset[::])
                return 
            
            # ALL SUBSETS WITH NUMS[I]
            subset.append(nums[i])
            back(i + 1, subset)
            subset.pop()
            
            # ALL SUBSETS WITHOUT NUMS[I]
            while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            back(i + 1, subset)
        
        back(0, [])
        return res