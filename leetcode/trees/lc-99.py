from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# started after looking at .cn idea but not solution
# start to AC - 15:18
# AC
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        # actually do not have to have 2 pairs # *
        # if there are 2 pairs, you know that the 2 wrong nodes must be the 1st of first pair and 2nd of second
        # so you can only store these 2 values and exchange
        wrong_pair1, wrong_pair2 = None, None

        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            nonlocal prev, wrong_pair1, wrong_pair2
            
            dfs(node.left)

            if prev and prev.val >= node.val:
                if not wrong_pair1:
                    wrong_pair1 = (prev, node) 
                else:
                    wrong_pair2 = (prev, node)
                    return # can return early here since there can be at most 2 pairs # *

            prev = node

            dfs(node.right)

        dfs(root)

        if not wrong_pair2:
            wrong_pair1[0].val, wrong_pair1[1].val = wrong_pair1[1].val, wrong_pair1[0].val
        else: # you initially did not put the line below in the else, which is a logic error # *
            wrong_pair1[0].val, wrong_pair2[1].val = wrong_pair2[1].val, wrong_pair1[0].val

        return root
