# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # Step 1: remember where each value sits in inorder
        position = {}
        for i in range(len(inorder)):
            position[inorder[i]] = i

        # Step 2: pre_index is the next root to take from preorder
        pre_index = [0]

        def build(left, right):
            # no nodes in this range
            if left > right:
                return None

            # take the next root from preorder
            root_value = preorder[pre_index[0]]
            pre_index[0] = pre_index[0] + 1
            root = TreeNode(root_value)

            # find the root in inorder
            mid = position[root_value]

            # build left first, then right
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)