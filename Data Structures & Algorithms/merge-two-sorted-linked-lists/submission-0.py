# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = node = ListNode()
        cur1 = list1
        cur2 = list2

        while cur1 != None and cur2 != None:
            if cur1.val < cur2.val:
                node.next = cur1
                cur1 = cur1.next
            else:
                node.next = cur2
                cur2 = cur2.next
            node = node.next
        node.next = cur1 or cur2
        return res.next