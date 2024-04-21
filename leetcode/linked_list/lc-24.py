from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# use pointers approach (after reading officla .cn solution)
# start to AC - 12:08
# AC
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dhead = ListNode(val=0, next=head)
        cur = dhead

        while cur.next and cur.next.next:
            next1, next2 = cur.next, cur.next.next
            cur.next = next2
            next1.next = next2.next
            next2.next = next1
            cur = next1
        
        return dhead.next
