# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lvl=0
        res = []

        def traversal(node,lvl):
            if node == None:
                return
            nonlocal res
            if len(res) < lvl+1:
                res.append([])
            res[lvl].append(node.val)
            traversal(node.left,lvl+1)
            traversal(node.right,lvl+1)
        traversal(root, 0)
        return res
        

        