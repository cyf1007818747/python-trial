# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        trav_right = True
        q = [root]
        rtn = []

        while q:
            li = []
            q_len = len(q)

            for i in range(q_len):
                # bfs must pop from the front (otherwise it's dfs) !! # *
                node = q.pop(0)
                li.append(node.val)
                if trav_right:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
                        
            q = q[::-1]
            trav_right = not trav_right
            rtn.append(li)

        return rtn
