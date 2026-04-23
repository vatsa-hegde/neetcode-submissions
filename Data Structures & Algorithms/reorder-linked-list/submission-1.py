# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return
        fast = head
        slow = head
        prev = None
        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        behind = None
        while slow != None:
            temp = slow
            slow = slow.next
            temp.next = behind
            behind = temp
        
        cur = head

        while cur !=None and behind != None:
            temp = cur
            cur = cur.next
            temp.next = behind
            behind = behind.next
            temp.next.next = cur
        if behind:
            temp.next.next = behind



            
        