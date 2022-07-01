class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x:x[1], reverse=1)
        
        res = 0
        
        for b, n in boxTypes:
            boxes = min(b,truckSize)
            
            res += boxes * n
            truckSize -= boxes
            if truckSize <= 0:
                return res
        
        return res
        