# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res=0
        
        def dfs(root):
            if root==None:
                return "covered_without_camera"

            left,right=dfs(root.left),dfs(root.right)
            
            if left==right=="covered_without_camera":
                return "to_be_covered"

            elif left=="to_be_covered" or right=="to_be_covered":
                self.res+=1
                return "covered_with_camera"

            elif left=="covered_with_camera" or right=="covered_with_camera":
                return "covered_without_camera"
        
        if dfs(root)=="to_be_covered":
            return 1+self.res
        
        return self.res