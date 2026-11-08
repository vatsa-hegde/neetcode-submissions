# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(root, prev_max):
            if root == None:
                return 0
            result = 0
            if root.val >= prev_max:
                result += 1
                prev_max = root.val
            return result + dfs(root.left,prev_max) + dfs(root.right,prev_max)

        return dfs(root, -101)

        """
           3
         3   None
        4 2
        """