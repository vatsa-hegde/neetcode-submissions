# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        close = abs(root.val-target)
        res = root.val

        left = right = root.val
        if root.left and target < root.val:
            left = self.closestValue(root.left,target)
        if root.right and target > root.val:
            right = self.closestValue(root.right,target)
        
        if abs(target-left) < close:
            res = left
            close = abs(target-left)
        if abs(target-right) < close:
            res = right
            close = abs(target-right)
        return res


        
        