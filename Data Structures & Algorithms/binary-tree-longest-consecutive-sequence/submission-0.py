# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node,length):
            nonlocal res
            print(length)
            if length > res:
                res = length
            if node.left:
                if node.left.val - node.val == 1:
                    dfs(node.left, length + 1)
                else:
                    dfs(node.left,0)
            if node.right:
                if node.right.val - node.val == 1:
                    dfs(node.right, length + 1)
                else:
                    dfs(node.right, 0)
        
        dfs(root, 0)
        return res+1

                

        