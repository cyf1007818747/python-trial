# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def helper func
# given a node, exchange left and right node
# then apply helper to left and right node as well
# passed all leetcode tests
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node: Optional[TreeNode]):
            if not node:
                return
            
            node.left, node.right = node.right, node.left

            helper(node.left)
            helper(node.right)

        helper(root)
        return root