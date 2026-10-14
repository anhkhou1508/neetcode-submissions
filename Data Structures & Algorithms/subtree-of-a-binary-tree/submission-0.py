# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #loop through tree to find same val nodes
        candidates = []
        stack_working = [root]
        while stack_working:
            node = stack_working.pop()
            if node.val == subRoot.val:
                candidates.append(node)
            if node.left:
                stack_working.append(node.left)
            if node.right:
                stack_working.append(node.right)
        
        #compare sub trees
        for candidate in candidates:
            if self.isSame(candidate, subRoot):
                return True
        return False

    def isSame(self, p, q):
        stack = [(p, q)]
        while stack:
            a,b = stack.pop()
            if not a and not b:
                continue
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            stack.append((a.left, b.left))
            stack.append((a.right, b.right))
        return True

        