from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# use slow and fast pointers
# d -> 1-2-3-4
# d -> 1-2-3-4-5

# start to AC - 19:30
# AC
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dhead = ListNode(val=0, next=head)
        fast, slow = dhead, dhead
        count = 0
        prev = dhead


        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
            count += 1

        li_len = count * 2 if fast else count * 2 - 1
        if n < count:
            gap = li_len - n - count + 1
        else:
            prev = dhead
            slow = head
            gap = li_len - n

        while gap:
            prev = slow
            slow = slow.next
            gap -= 1

        prev.next = slow.next
        return dhead.next
    

# use better slow and fast pointers, where fast surpasses slow n nodes
# (after seeing officialn .cn solution)
# 1-2-3-4-5
# start to AC - 3:36
# AC
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dhead = ListNode(val=0, next=head)
        fast, slow = dhead, dhead
        prev = None

        while n > 0:
            fast = fast.next
            n -= 1
        
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
        
        prev.next = slow.next
        return dhead.next
