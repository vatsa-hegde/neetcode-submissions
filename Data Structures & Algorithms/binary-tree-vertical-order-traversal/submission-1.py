# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        res = []
        q = deque([(root,0)])

        while q:
            ele,idx = q.popleft()
            if ele == None:
                continue
            d[idx].append(ele.val)
            q.append((ele.left, idx-1))
            q.append((ele.right,idx+1))

        # print(d)
        for x in sorted(d.keys()):
            res.append(d[x])
        return res


        