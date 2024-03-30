from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# bfs, layer to later, and traverse from right to left
# always overwrite the previous leftmost with the newly traversed node
# the final node is what we want
class Solution:
    # passed all leetcode tests
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = 0

        # bfs
        q = [root]
        while q:
            node = q.pop(0)
            ans = node.val
            if node.right:  # remember to check this !! # *
                q.append(node.right)
            if node.left:
                q.append(node.left)

        return ans

# dfs approach (just to practice)
# def a dfs func
# > not node: ...
# if the node depth > max depth, update max depth and cur val
# dfs childs
class Solution2:
    # passed all leetcode tests
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        curVal = root.val

        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return
            
            nonlocal maxDepth, curVal

            if depth > maxDepth:
                maxDepth = depth
                curVal = node.val

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0)
        return curVal

            
# traverse from left to right and use collections.deque (just to practice)
class Solution3:
    # passed all leetcode tests
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        if not root:
            return 0
        
        ans = 0

        q = deque([root])

        while q: 
            len_q = len(q)
            for i in range(len_q):  # this is the way to distinguish between layers # *
                node = q.popleft()
                if i == 0:
                    ans = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ans

                
