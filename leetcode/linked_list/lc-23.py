from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# initialize a dummy head
# use a heap to store the heads of lists
# while the heap is not none, pop the top, append to the tail, and push the pop.next if not None
class NodeWrapper:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other):
        # // self.node.val < other.node.val
        return self.node.val < other.node.val # very silly mistake # *


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        hp = [ NodeWrapper(nd) for nd in lists if nd ]
        heapq.heapify(hp)

        dhead = ListNode()
        cur = dhead

        while hp:
            top = heapq.heappop(hp).node
            cur.next = top
            cur = cur.next
            if top.next:
                heapq.heappush(hp, NodeWrapper(top.next))
        
        return dhead.next
