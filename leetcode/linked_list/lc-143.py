from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# use most straight forward indexing list approach
# start to AC - 12:19
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []

        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        length = len(nodes)
        for i in range(length // 2):
            nodes[i].next = nodes[length - i - 1]
            if length - i - 1 != i+1:
                nodes[length - i - 1].next = nodes[i+1]
            else:
                nodes[length - i - 1].next = None
            # this error will not affect nodes[i+1], since nodes[i+1] is corrected int the next loop
            # yet, the only difference of this compares to the correct solution is there is a loop not removed
            # which causes the final test infinite
            # // if length - i - 1 != i+2:
            if length - i - 1 == i+2:
                nodes[i+1].next = None

# use O(1) time complexity (after seeing .cn solution)
# 1-2
# 1-2-3
# start to AC - 29:02
# AC
class Solution2:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverseList(node: Optional[ListNode]):
            if not node or not node.next:
                return node

            dhead = None
            pre, cur = dhead, node
            while cur:
                org_next = cur.next
                cur.next = pre
                # details ! pay attention # *
                # // pre, cur = cur, cur.next
                pre, cur = cur, org_next

            return pre

        # return smallest mid if multiple mids
        def findMid(node: Optional[ListNode]):
            if not node or not node.next:
                return node

            # you can directly write slow = fast = head in Python # *
            slow, fast = node, node
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def mergeLists(node1: Optional[ListNode], node2: Optional[ListNode]):
            nd1, nd2 = node1, node2
            dhead = ListNode(0)
            cur = dhead
            while nd1 and nd2:
                org_nd1_next = nd1.next
                cur.next = nd1
                cur = cur.next
                cur.next = nd2
                # cannot make cur to be None eventually
                # otherwise not able to track the tail, thus append the rest to tail
                # // cur = cur.next
                if cur.next:
                    cur = cur.next
                # you forgot that nd1.next was changed to nd2
                # // nd1, nd2 = nd1.next, nd2.next
                nd1, nd2 = org_nd1_next, nd2.next
            
            if nd1:
                cur.next = nd1
            elif nd2:
                cur.next = nd2

            return dhead.next

        midnode = findMid(head)
        reversed_half = reverseList(midnode.next)
        midnode.next = None
        mergeLists(head, reversed_half)
