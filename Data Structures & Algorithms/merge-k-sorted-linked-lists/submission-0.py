# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0 or lists[0] == None:
            return None
        def merge(a, b):
            if not a or not b:
                return a if a else b
            cur1 = a
            cur2 = b
            res = ListNode()
            head = res
            while cur1 and cur2:
                if cur1.val >= cur2.val:
                    head.next = cur2
                    cur2 = cur2.next
                else:
                    head.next = cur1
                    cur1 = cur1.next
                head = head.next
            if cur1:
                head.next = cur1
            elif cur2:
                head.next = cur2
            return res.next
        for i in range(1,k):
            lists[i] = merge(lists[i-1], lists[i])
        return lists[-1]

        