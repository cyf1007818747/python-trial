from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# start to AC - 14:09
# AC
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk1, stk2 = [], []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        while l2:
            stk2.append(l2.val)
            l2 = l2.next
        
        cur = None
        leftover = 0
        
        while stk1 or stk2:
            summ = 0
            # avoid using this ambiguous syntax in interviews
            # // summ += stk1.pop() if stk1 else None
            # // summ += stk2.pop() if stk2 else None
            if stk1:
                summ += stk1.pop()
            if stk2:
                summ += stk2.pop()
            summ += leftover
            nd = ListNode(summ % 10)
            # logical error ! # *
            # // leftover = summ - (summ % 10) 
            leftover = summ // 10
            nd.next = cur
            cur = nd
        
        if leftover > 0:
            cur = ListNode(val=leftover, next=cur)

        return cur
