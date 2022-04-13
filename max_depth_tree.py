
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Example 1:


# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: 3


# Definition for a binary tree node.

from collections import deque

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return False

        # return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))

        n = deque([root])
        level = 0

        while n:
            for i in range(len(n)):
                node = n.popleft()
                if node.right:
                    n.append(node.right)
                if node.left:
                    n.append(node.left)

            level += 1

        return level
