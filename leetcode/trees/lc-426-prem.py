from typing import Optional

"""
Question:
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor 
pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the 
first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the 
tree node should point to its predecessor, and the right pointer should point to its successor. 
You should return the pointer to the smallest element of the linked list.
"""

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# in-order dfs the tree, and save prev, head and last
# link prev and current for each search
# link head and tail

# start to AC - 14:22
# AC
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        head, prev = None, None
        
        def dfs(nd: Node):
            if not nd:
                return

            nonlocal head, prev # you forgot this line again initially # *

            dfs(nd.left)

            if not head:
                head = nd

            if prev:
                prev.right = nd
                nd.left = prev

            prev = nd

            dfs(nd.right)

        dfs(root)

        head.left, prev.right = prev, head
        return head
