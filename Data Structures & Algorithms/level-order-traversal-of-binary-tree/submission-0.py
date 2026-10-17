# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, 1)]
        result = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(result) < level:
                    result.append([node.val])
                else:
                    result[level-1].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        
        return result


    
#      3
#     / \
#    9.  20
#        / \
#       15. 7

# stack = [(7,3),(15,3)]
        
# result = [[3],[9,20]]. len: 2
          