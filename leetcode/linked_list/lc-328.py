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

# write again on April 21
# start to AC - 18:09
# AC
class Solution2:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        odd_dhead = ListNode(0)
        even_dhead = ListNode(0)
        odd_tail, even_tail = odd_dhead, even_dhead

        # cur is always odd index
        while cur:
            odd_tail.next = cur
            if cur.next:
                even_tail.next = cur.next
            else:
                odd_tail = odd_tail.next
                break
            cur = cur.next.next
            odd_tail, even_tail = odd_tail.next, even_tail.next

        odd_tail.next, even_tail.next = even_dhead.next, None
        return odd_dhead.next


# use 2 pointers after reading official solution
# 1 - 2 - 3 - 4
# 1 - 2 - 3 - 4 - 5
class Solution3:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        odd, even = head, head.next
        even_head = even

        while odd and odd.next:
            odd.next = even.next
            if odd.next:
                even.next = odd.next.next
            else:
                break
            odd, even = odd.next, even.next

        odd.next = even_head
        return head
