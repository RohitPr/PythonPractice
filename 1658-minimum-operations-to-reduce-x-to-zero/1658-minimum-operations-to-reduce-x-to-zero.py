class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
#         toFind = sum(nums) - x
        
#         l = 0
#         res = -1
        
#         for r in range(len(nums)):
#             toFind -= nums[r]
#             while toFind < 0:
#                 toFind += nums[l]
#                 l += 1
            
#             if toFind == 0:
#                 res = max(res, r-l +1)
        
#         return (len(nums) - res) if res != -1 else -1

            N = len(nums)
            toremove = sum(nums) - x
            if toremove < 0: return -1

            longest_removal = -1
            left = 0
            for right in range(N):
                toremove -= nums[right]
                while toremove < 0:
                    toremove += nums[left]
                    left += 1
                if toremove == 0:
                    longest_removal = max(longest_removal, right - left + 1)

            return N - longest_removal if longest_removal != -1 else -1

