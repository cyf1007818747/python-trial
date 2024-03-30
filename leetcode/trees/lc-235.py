# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# try to find the paths to p and q
# the last common node is the lowest ancestor
        
# def dfs: given a node, a target
# if not node (will not happen in this q): return
# path.append(node)
# > if node.val == target: return
# > if node.val < target: dfs(node.right)
# > if node.val > target: dfs(node.left)
# compare the 2 paths, find the last common one (use zip)

# passed all leetcode tests
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node: 'TreeNode', target: int, path: List[TreeNode]):
            if not node:
                return
            
            path.append(node)
            
            if node.val == target:
                return
            elif node.val < target:
                dfs(node.right, target, path)
            else:
                dfs(node.left, target, path)

        path_p = []
        path_q = []

        dfs(root, p.val, path_p)
        dfs(root, q.val, path_q)

        for item in reversed(list(zip(path_p, path_q))): # *
            if len(item) > 1 and item[0] == item[1]:
                return item[0]
            
        return None
