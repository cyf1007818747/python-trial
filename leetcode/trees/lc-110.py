from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# passed all leetcode tests
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return balancedNodeDepth(root) != -1

# if return >= 0: node is balanced, the returned num is height
# if return == -1: node is imbalanced
def balancedNodeDepth(node: Optional[TreeNode]) -> int:
    if not node:
        return 0
    
    leftDepth = balancedNodeDepth(node.left)
    rightDepth = balancedNodeDepth(node.right)
    if leftDepth == -1 or rightDepth == -1 or abs(leftDepth - rightDepth) > 1:
        return -1

    return 1 + max(leftDepth, rightDepth)