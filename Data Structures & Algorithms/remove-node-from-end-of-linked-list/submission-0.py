# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        cur = head
        N = 0
        while cur != None:
            N+=1
            cur = cur.next
        cur = head
        prev = ListNode()
        if N-n == 0:
            return head.next
        for i in range(N-n):
            prev = cur
            cur = cur.next
        prev.next = cur.next if cur else None
        print(prev.val)
        return head
        