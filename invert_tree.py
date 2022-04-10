# Given the root of a binary tree, invert the tree, and return its root.

# Input: root = [4, 2, 7, 1, 3, 6, 9]
# Output: [4, 7, 2, 9, 6, 3, 1]


def invertTree(self, root):
    if root:
        root.left, root.right = self.invertTree(
            root.right), self.invertTree(root.left)
        return root


def invertTree(self, root):
    if root:
        invert = self.invertTree
        root.left, root.right = invert(root.right), invert(root.left)
        return root

#  Iterative Stack


def invertTree(self, root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right
    return root
