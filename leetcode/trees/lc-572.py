from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def helper: areTreesEqual(rt1, rt2)
# > if both are None: return True
# > if only one of them is None: return false
# > else (both are not none):
# >> if values are not equal: return false
# >> else return areTreesEqual(left childs) and areTreesEqual(right childs)
        
# for the main function: apply the above func to all tht nodes in root1 and subRoot
# if any returns True then the final return is True (! can early return)
# > if not root: return a-t-e(root, subRoot)
# > if root: return a-t-e(root, SubRoot) or isSubTree(root.left, SubRoot) or isSubTree(root.right, SubRoot)
# passed all leetcode tests, but very slow due to O(N^2) time complexity
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def areTreesEqual(rt1: Optional[TreeNode], rt2: Optional[TreeNode]) -> bool:
            if not rt1 and not rt2:
                return True
            
            if ((not rt1) and rt2) or (rt1 and (not rt2)):
                return False
            
            # else case: both are not none
            if rt1.val != rt2.val:
                return False
            
            return areTreesEqual(rt1.left, rt2.left) and areTreesEqual(rt1.right, rt2.right)
        
        if not root:
            return areTreesEqual(root, subRoot)
        
        return areTreesEqual(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
