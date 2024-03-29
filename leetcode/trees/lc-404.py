from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def a helper func: given a node
# > if its left is not none: >> has no child, add to the sum
# apply the helper on left and right
# passed all leetcode tests
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        summ = [0]

        def helper(node: Optional[TreeNode]):
            if not node:
                return
            
            if node.left and not node.left.left and not node.left.right:
                summ[0] += node.left.val

            helper(node.left)
            helper(node.right)

        helper(root)

        return summ[0]


# use nonlocal variabl summ
# passed all leetcode tests
class Solution2:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        summ = 0

        def helper(node: Optional[TreeNode]):
            if not node:
                return
            
            nonlocal summ
            
            if node.left and not node.left.left and not node.left.right:
                summ += node.left.val

            helper(node.left)
            helper(node.right)

        helper(root)

        return summ
    
# use class attribute
# passed all leetcode tests
class Solution3:
    def __init__(self):
        self.sum = 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(node: Optional[TreeNode]):
            if not node:
                return
            
            if node.left and not node.left.left and not node.left.right:
                self.sum += node.left.val

            helper(node.left)
            helper(node.right)

        helper(root)

        return self.sum
    
# use function accumulation, without helper function
# NOTE: This one is not as easy to think as above, so use above if you feel more straightforward
# just recite how to write like this way if the code is hard to understand
# passed all leetcode tests
class Solution4:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        sum = 0

        if root.left and not root.left.left and not root.left.right:
            sum += root.left.val

        return sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

