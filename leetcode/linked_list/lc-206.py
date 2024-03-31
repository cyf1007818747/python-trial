from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# non-recursive (most straightforward approach)
# > if len head <= 1
    # not head: return None
    # not head.next > return head

# initialize prev to be None
# for each node:
# > if node: node.next = prev, prev = node, then reverse node.next
# > if not node: stop
# passed all leetcode tests
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev, ptr = None, head

        # TODO: the reason why below is wrong is to be investigated
        # while ptr: 
        #     prev, ptr, ptr.next = ptr, ptr.next, prev # ! wrong

        while ptr:
            next_node = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next_node

        return prev
    
# recursive approach (just to practice)
# if not head: return None
# for each node:
# > if next: 1. get the reversed next (where next.next is not reversed)  2. make next.next = node  3. return node
# > if not next: return node
# passed all leetcode tests (in 1 try)
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None

        def helper(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node:
                return None
            
            if node.next:
                reversed_next = helper(node.next)
                reversed_next.next = node
                return node
            else:
                nonlocal new_head
                new_head = node
                return node

        if not head:
            return None
        
        helper(head)
        head.next = None

        return new_head
    
# ! recite
# recursive approach - improved
# if not head: return None
# for each node:
# > if next: 1. reverse next (where next.next is not reversed)  2. make next.next = node  3. return new_head
# > if not next: return node
# passed all leetcode tests
class Solution3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None # *

        return new_head
        