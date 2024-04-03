from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# original trial, passed all leetcode solutions
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # the official .cn solution omit this step
        if not list1 and not list2:
            return None

        if not list1:
            return list2
        
        if not list2:
            return list1

        cur = ListNode(-1)
        head = cur

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next

        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2

        return head.next
    

# recursive approach
# passed all leetcode tests
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        

# use the official .cn approach that uses prev
# (similar to solution1, only slighlt different)
# passed all leetcode tests
class Solution3:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        head = ListNode(-1)
        # prev can also be called 'tail'
        prev = head

        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        prev.next = list1 if list1 else list2

        return head.next