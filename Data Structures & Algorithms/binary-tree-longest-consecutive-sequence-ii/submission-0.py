# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res

            if node == None:
                return [0,0]
            inc = dec = 1
            if node.left:
                left = dfs(node.left)
                if node.val - 1 == node.left.val:
                    dec += left[0]
                elif node.val +1 == node.left.val:
                    inc += left[1]
            
            if node.right:
                right = dfs(node.right)
                if node.val - 1 == node.right.val:
                    dec += right[0]
                elif node.val + 1 == node.right.val:
                    inc += right[1]
            res = max(res,inc+dec-1)
            return [dec, inc]
        dfs(root)
        return res

            

                

        

            
            

                    