class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        count = {}
        res = []
        
        for a in nums1:
            count[a] = 1 + count.get(a, 0)
        
        for b in nums2:
            if b in count and count[b] > 0:
                res.append(b)
                count[b] -= 1
        
        return res