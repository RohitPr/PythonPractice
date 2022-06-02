class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROW, COLS = len(matrix), len(matrix[0])
        
        res = []
        
        for col in range(COLS):
            temp = []
            for row in range(ROW):
                temp.append(matrix[row][col])
            res.append(temp)
                
        return res
    
#     return list(zip(*matrix))