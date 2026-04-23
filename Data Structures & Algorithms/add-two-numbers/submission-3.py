# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        c = 0
        prev = None
        while cur1 != None and cur2!= None:
            cur1.val += cur2.val + c
            c = cur1.val // 10
            cur1.val %= 10
            prev = cur1
            cur1 = cur1.next
            cur2 = cur2.next

        if not cur1:
            prev.next = cur2
            while cur2:
                cur2.val+= c
                if cur2.val > 9:
                    c = cur2.val // 10
                    cur2.val %= 10
                else:
                    c = 0
                    break
                prev = cur2
                cur2 = cur2.next
        if cur1 and c:
            while c > 0 and cur1:
                # print(cur1.val,c)
                cur1.val += c
                c = cur1.val // 10
                cur1.val %= 10
                prev = cur1
                cur1 = cur1.next 

        if c > 0:
            prev.next = ListNode(c)
        return l1
        