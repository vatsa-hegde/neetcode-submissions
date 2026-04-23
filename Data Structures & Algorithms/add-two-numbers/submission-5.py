# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1,l2
        res = curres = ListNode()
        carry = 0
        while cur1 and cur2:
            temp = ListNode((cur1.val+cur2.val + carry) % 10)
            carry = (cur1.val+cur2.val+carry) // 10
            curres.next = temp
            cur1, cur2, curres = cur1.next,cur2.next, curres.next
        while cur1:
            temp = ListNode((cur1.val+carry)%10)
            carry = (cur1.val+carry) // 10
            curres.next = temp
            curres = curres.next
            cur1 = cur1.next
        while cur2:
            temp = ListNode((cur2.val+carry)%10)
            carry = (cur2.val+carry) // 10
            curres.next = temp
            curres = temp
            cur2 = cur2.next
        if carry:
            curres.next = ListNode(carry)
        return res.next
            

        