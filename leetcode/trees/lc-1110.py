# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def helper func to check a given node
# input: a TreeNode, to_delete list
# return: modified node
# for a given node, modifies the left and right node
# > if self node is to be deleted: 1. add all not none child node to the rtn list 2. return none
# > if self node is not to be deleted: make the left and right node to be the modified nodes

# passed all leetcode cases
def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    ans = []

    def helper(node: TreeNode) -> Optional[TreeNode]:
        if not node:
            return None
        
        left = helper(node.left)
        right = helper(node.right)

        if node.val in to_delete:
            if left:
                ans.append(left)
            if right:
                ans.append(right)
            return None
        else:
            node.left = left
            node.right = right
            return node

    modified_root = helper(root)

    if modified_root:
        ans.append(modified_root)

    return ans
            

