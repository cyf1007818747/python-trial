from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# bfs the original tree
# each time, iterate all but the last node in a later, make node.next point to the next element
# start to AC - 10:35
# AC
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q = [root]

        while q:
            # you made this mistake again !! # *
            # in bfs, the length of the queue is changing, so you cannot use it in the loop
            # // for i in range(len(q)):
            # //    if i < len(q) - 1:
            len_q = len(q)
            for i in range(len_q):
                if i < len_q - 1:
                    q[0].next = q[1]
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                del q[0]
        
        return root
 

# use pointers to save space complexity (after reading .cn solution)
# start to AC - 4:39
# AC
class Solution2:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        layer_left = root

        # do not have to traverse the leaves, since links are built at parents
        while layer_left.left:
            
            cur = layer_left

            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left

                cur = cur.next

            layer_left = layer_left.left

        return root
