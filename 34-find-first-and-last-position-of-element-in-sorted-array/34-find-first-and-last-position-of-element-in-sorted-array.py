class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binSearch(nums, target, flag):
            res, l, r = -1, 0, len(nums) - 1
            
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    res = mid
                    if flag:
                        l = mid + 1
                    else:
                        r = mid - 1
                        
                elif nums[mid] > target:
                    r = mid - 1

                else:
                    l = mid + 1
            return res

        left, right = binSearch(nums, target, False), binSearch(nums, target, True) 
        
        return [left, right] 