# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traversal(node, lvl):
            nonlocal res
            if not node:
                return
            if len(res) < lvl+1:
                res.append(node.val)
            else:
                res[lvl] = node.val
            traversal(node.left,lvl+1)
            traversal(node.right, lvl+1)
        traversal(root,0)
        return res
        