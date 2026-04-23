"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        visit = {}
        def traversal(cur):
            if cur.val in visit:
                return visit[cur.val]
            n = Node(cur.val)
            visit[cur.val] = n
            for nei in cur.neighbors:
                n.neighbors.append(traversal(nei))
            return n
        return traversal(node)


        