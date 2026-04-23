# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def traversal(node, highest):
            if not node:
                return
            nonlocal res
            if node.val >= highest:
                res+= 1
                highest = node.val
            traversal(node.left, highest)
            traversal(node.right, highest)
        traversal(root,root.val)
        return res
        