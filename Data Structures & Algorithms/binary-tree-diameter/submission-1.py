# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            # print(root.val,l,r,res)
            if l+r > res:
                res = l+r
            # print(res)
            return max(l+1, r+1)
        tmp = dfs(root)
        res= max(res,tmp-1)
        # res = max(res,dfs(root)-1)
        return res