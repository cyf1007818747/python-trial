from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# num nodes <= 1: return head
# traverse the list, for each cur:
# > if not cur: none
# > if not cur.next: none
# > else: if cur == cur.next: cur.next = cur.next.next
# > else: cur = cur.next
# passed all leetcode cases
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head
        
