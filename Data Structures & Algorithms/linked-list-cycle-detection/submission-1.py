# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return False
        l = r = head
        while r != None:
            # print(l, r)
            l = l.next
            r = r.next
            if r:
                r = r.next
            if l == r:
                return True
            # print(l, r)
        return False
        