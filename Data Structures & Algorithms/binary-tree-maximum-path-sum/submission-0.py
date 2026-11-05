# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        best = float('-inf')          # the scoreboard

        def go(node):
            nonlocal best
            if not node:
                return 0

            # one-side value from each child; skip it if it's negative
            left = max(0, go(node.left))
            right = max(0, go(node.right))

            # Question B: this node is the top, use both sides
            best = max(best, node.val + left + right)

            # Question A: what we report up to the parent (one side only)
            return node.val + max(left, right)

        go(root)
        return best