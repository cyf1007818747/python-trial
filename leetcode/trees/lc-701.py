from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# start to AC - 6:05
# AC
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def recur_insert(node: Optional[TreeNode], v: int):
            if v > node.val:
                if node.right:
                    recur_insert(node.right, v)
                else:
                    node.right = TreeNode(v)
                    return
            if v < node.val:
                if node.left:
                    recur_insert(node.left, v)
                else:
                    node.left = TreeNode(v)
                    return
        
        if not root:
            return TreeNode(val)

        recur_insert(root, val)

        return root
    

# use pointer / non-recursive approach
# start to AC - 3:11
# AC
class Solution2:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        ptr = root
        while ptr:
            if val > ptr.val:
                if ptr.right:
                    ptr = ptr.right
                else:
                    ptr.right = TreeNode(val)
                    return root
            elif val < ptr.val:
                if ptr.left:
                    ptr = ptr.left
                else:
                    ptr.left = TreeNode(val)
                    return root
        
        return root