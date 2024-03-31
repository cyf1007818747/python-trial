from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# // if num nodes <= 1: return head
# //define 2 heads: head_odd. head_even
# //travers the list, for each node cur:
# //> if it is none: /
# //> if it is odd, concat to the tail of head_odd, odd_tail = cur, cur = cur.next
# //> if it is even, concat to the tail of head_even, even_tail = cur, cur = cur.next
# //finally, concat the head of even to the tail of odd, and return the head of odd
# //consider 3 differnet cases:
# //> None, head
# //> head, None
# //> else
# you completely misunderstood the question, so the solution is very weird
# passed all leetcode tests
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd_head, even_head = None, None
        odd_tail, even_tail = odd_head, even_head

        cur = head
        index = 0
        while cur:
            # odd
            if index % 2 == 1:
                if not odd_head:
                    odd_head = cur
                    odd_tail = odd_head
                else:
                    odd_tail.next = cur
                    odd_tail = cur
            # even
            else:
                if not even_head:
                    even_head = cur
                    even_tail = even_head
                else:
                    even_tail.next = cur
                    even_tail = cur
            cur = cur.next
            index += 1

        # *
        # ! below is important ro remove cycle, since you directly modify the given list
        if odd_tail:
            odd_tail.next = None
        if even_tail:
            even_tail.next = None

        if odd_head and even_head:
            even_tail.next = odd_head
            return even_head
        elif odd_head and not even_head:
            return odd_head
        else:
            return even_head
                