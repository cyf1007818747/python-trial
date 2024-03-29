from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# in the recursive calls of the func, always merge 2 nodes in the matching positions
# > if root1 and root2: 
#   1. root1.val += root2.val
#   2. merge the left childs and right childs of 2 roots, and make the left and right of root1 equals them
#   3. return root1
# > if one of them is None, return the other (no matter the other is none or not)
# passed all leetcode tests
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            root1.val += root2.val
            root1.left, root1.right = self.mergeTrees(root1.left, root2.left), self.mergeTrees(root1.right, root2.right)
            return root1
        elif not root1:
            return root2
        else:
            return root1