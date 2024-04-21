from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# use .cn O(nlogn) solution 1
# def convert: given a linked list, return the root of the converted balanced BST
# 1-2-3
# 1-2-3-4
# start to AC - 13:28
# AC
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def convert(li_nd: Optional[ListNode]):
            # both 2 special cases below should both be considered # *
            if not li_nd:
                return None
            
            if not li_nd.next:
                return TreeNode(li_nd.val)
            
            slow, fast = li_nd, li_nd
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            prev.next = None
            left = convert(li_nd)
            right = convert(slow.next)
            return TreeNode(val=slow.val, left=left, right=right)
        
        return convert(head)
