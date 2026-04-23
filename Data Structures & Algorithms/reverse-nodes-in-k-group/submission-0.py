# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        res = ListNode()
        res.next = head
        l = 0
        while cur != None:
            l+=1
            cur = cur.next
        l = l // k
        i = 0
        prev = None
        lp = res
        cur = head
        while cur != None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            # print(cur.val,nxt)
            cur = nxt
            i+=1
            if i == k:
                tmp = lp.next
                lp.next = prev
                tmp.next = cur
                prev = None
                lp = tmp
                i = 0
                l -= 1
                if l == 0:
                    lp.next = cur
                    break
        
        return res.next
