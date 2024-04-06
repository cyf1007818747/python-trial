from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# non-recursive hash map solution (after seeing the idea of others' solution)
# start to AC - 7:38
# AC
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_to_new = {}

        cur = head
        while cur:
            old_to_new[cur] = Node(x = cur.val)
            cur = cur.next

        for key in old_to_new:
            if key.next: # *
                old_to_new[key].next = old_to_new[key.next]
            if key.random: # *
                old_to_new[key].random = old_to_new[key.random]

        return old_to_new[head]


# recursive solution
# start to AC: 7:29
# AC
class Solution2:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}

        def recursiveCopy(node: Node):
            if not node:
                return None
            
            nonlocal old_to_new

            if old_to_new.get(node) == None:
                new_node = Node(node.val)
                old_to_new[node] = new_node # *
                new_node.next = recursiveCopy(node.next)
                new_node.random = recursiveCopy(node.random)
                return new_node
            else:
                return old_to_new[node]

        return recursiveCopy(head)


# use O(1) space, non-recursive, very tricky approach
# 1. copy by duplicating node and chaining them
# A -> B -> C -> None
# A -> A' -> B -> B' -> C -> C' -> None

# 2. for the random, each new node points to the next of the random of original node
#   - e.g. if A random to C, then A' random to the next of A random, which is the next of C, which is C'

# 3. make the next in the copied list correct, and restore the original linked listx
# careful for edge cases !!

# start to AC while orally mocking interview - 24:43
# AC
class Solution3:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        cur = head
        while cur:
            # general case
            org_next = cur.next
            cur.next = Node(cur.val)
            cur.next.next = org_next
            cur = org_next

        cur = head
        while cur:
            # general case
            org_random = cur.random
            self_copy = cur.next
            if org_random:
                self_copy.random = org_random.next
            else:
                self_copy.random = None

            cur = cur.next.next

        cur = head
        new_head = cur.next

        while cur:
            # general case
            self_copy = cur.next
            cur.next = cur.next.next
            if self_copy.next:
                self_copy.next = self_copy.next.next

            cur = cur.next # you forgot initially # *
        
        return new_head
