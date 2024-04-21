from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# start to AC - 17:24
# AC
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        smaller_dhead = ListNode()
        smaller_tail = smaller_dhead

        # wrong !!! # *
        # // dhead = ListNode(head)
        dhead = ListNode(next=head)
        prev = dhead
        cur = head

        while cur:
            if cur.val < x:
                # remove
                prev.next = cur.next
                # insert
                smaller_tail.next = cur
                smaller_tail = smaller_tail.next
            # logic error !! only proceed prev if do not have to remove element # *
            #//prev = cur
            #//cur = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
            

        smaller_tail.next = dhead.next
        return smaller_dhead.next
