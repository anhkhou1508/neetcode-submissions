# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        bestDepth = 0
        if not root:
            return 0
        stack.append((root, 1))
        while stack:
            node, level = stack.pop()
            bestDepth = max(bestDepth, level)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        
        return bestDepth