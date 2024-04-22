from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# use monotonic stack
# start to AC - 11:18
# AC
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        # instead of using gt_idx, a simpler approach is to append a 0 to ans each time,
        # so that the length of ans increases as we iterate over the loop

        # each element is: (node index, next greater node value)
        gt_idx = []
        stk = [] # (idx, node value)
        idx = 1
        
        while head:
            while stk and head.val > stk[-1][1]:
                top = stk[-1]
                gt_idx.append((top[0], head.val))
                stk.pop()
            # // stk.push((idx, head.val))
            stk.append((idx, head.val))
            head = head.next
            idx += 1
        
        ans = [0] * (idx - 1)
        for index, value in gt_idx:
            ans[index - 1] = value

        return ans
