"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        cur = head
        res = Node(0)
        prev = res
        while cur != None:
            temp = Node(cur.val,None, cur.random)
            prev.next = temp
            prev = prev.next
            d[cur] = temp
            cur = cur.next
        cur = res.next
        while cur!= None:
            if cur.random:
                cur.random = d.get(cur.random, None)
            cur = cur.next
        return res.next

            

        