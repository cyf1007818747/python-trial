from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# traverse the tree in descending order (inorder, right first)
# def dfs of a node:
# sum += node.val
# node.val = sum
# passed all leetcode tests
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:  
        sum = 0
        
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            
            dfs(node.right)

            nonlocal sum
            sum += node.val
            node.val = sum

            dfs(node.left)

        dfs(root)

        return root

