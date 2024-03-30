from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# traverse the tree in ascending order
# the min diff must be between 2 consecutive elements, since BST

# def dfs: inorder, left to right
# keep a record of the prev traversed value, if abs(curr - prev) < min_abs_diff, update
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # ! no int('inf') in python
        # //min_abs_diff = int('inf') raises error
        # // prev = int('inf') raises error
        min_abs_diff = float('inf')
        prev = float('inf')

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            
            nonlocal prev, min_abs_diff

            dfs(node.left)

            if abs(node.val - prev) < min_abs_diff:
                min_abs_diff = abs(node.val - prev)

            prev = node.val

            dfs(node.right)

        dfs(root) # you forget to add this many times # *

        return min_abs_diff