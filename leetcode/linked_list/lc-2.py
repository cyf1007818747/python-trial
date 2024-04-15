from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# start to AC - 15:17
# AC
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        p3 = ListNode(0)
        dummyhead = p3
        rmd = 0

        while p1 and p2:
            summ = p1.val + p2.val + rmd # try to use the same name as below for easier modification # *
            # this is wrong, because once p3 points to None, modifying it will no longer modify the tail of new List # *
            # // p3 = ListNode(summ % 10)
            # // rmd = summ // 10
            # // p1, p2, p3 = p1.next, p2.next, p3.next
            p3.next = ListNode(summ % 10)
            rmd = summ // 10
            p1, p2, p3 = p1.next, p2.next, p3.next

        while p1:
            summ = p1.val + rmd # *
            p3.next = ListNode(summ % 10)
            rmd = summ // 10
            p1, p3 = p1.next, p3.next

        while p2:
            summ = p2.val + rmd
            p3.next = ListNode(summ % 10)
            rmd = summ // 10
            p2, p3 = p2.next, p3.next

        if rmd:
            p3.next = ListNode(rmd)

        return dummyhead.next

# better code style
# AC, much faster running time
class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        p3 = ListNode(0)
        dummyhead = p3
        rmd = 0

        while p1 or p2:
            summ = rmd
            if p1:
                summ += p1.val
                p1 = p1.next
            if p2:
                summ += p2.val
                p2 = p2.next
            p3.next = ListNode(summ % 10)
            rmd = summ // 10
            p3 = p3.next

        if rmd:
            p3.next = ListNode(rmd)

        return dummyhead.next
