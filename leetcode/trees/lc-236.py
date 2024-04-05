# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 1. dfs to find 2 nodes, and record paths using backtracking
# 2. compare the 2 paths from last to front, the first equal one is
# from start to AC - 20:58
# AC
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathp = []
        pathq = []
        path = []

        def dfs(node: TreeNode):
            if not node:
                return
            
            # !! you made mistake many times
            nonlocal pathp, pathq, path # *

            path.append(node)

            if node == p:
                pathp = path.copy()
                # this is an edge case, where q is a child of p # *
                # //return
            
            if node == q:
                pathq = path.copy()
                # this is an edge case, where p is a child of q # *
                # // return

            dfs(node.left) 
            dfs(node.right)

            path.pop()

        dfs(root)

        i = 0
        while i < min(len(pathp), len(pathq)):
            if pathp[i] != pathq[i]:
                return pathp[i-1]
            i += 1

        # the common ancestor must now be the last element
        if i == len(pathp):
            return pathp[-1]
        else:
            return pathq[-1]

# improved final finding common node step
# AC, slightly slower than solution 1 since you have to assign to ans many timesxs
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathp = []
        pathq = []
        path = []

        def dfs(node: TreeNode):
            if not node:
                return
            
            nonlocal pathp, pathq, path

            path.append(node)

            if node == p:
                pathp = path.copy()
                # this is an edge case, where q is a child of p
                # //return
            
            if node == q:
                pathq = path.copy()
                # this is an edge case, where p is a child of q
                # // return

            dfs(node.left) 
            dfs(node.right)

            path.pop()

        dfs(root)

        ans = None
        for i in range(min(len(pathp), len(pathq))):
            if pathp[i] == pathq[i]:
                ans = pathp[i]
                
        return ans


# use simpler recursive approach and a left or right trick after check .cn solution
# this solution smartly covers the edge case
# AC
class Solution3:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def contains_porq(node: TreeNode) -> Optional[TreeNode]:
            if not node:
                return None

            if node == p or node == q:
                 return node

            contains_porq_l = contains_porq(node.left)
            contains_porq_r = contains_porq(node.right)

            if not contains_porq_l and not contains_porq_r:
                return None

            if contains_porq_l and contains_porq_r:
                return node
            
            return contains_porq_l if contains_porq_l else contains_porq_r

        return contains_porq(root)


# use simpler recursive approach and a left or right trick
# modified approach of solution3, modified by you to simpler the return type
# AC
class Solution4:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def contains_porq(node: TreeNode) -> bool:
            nonlocal ans

            if not node:
                return False

            if node == p or node == q:
                # edge case # !! you used 10 min to find this bug
                if contains_porq(node.left) or contains_porq(node.right):
                    ans = node
                return True

            contains_porq_l = contains_porq(node.left)
            contains_porq_r = contains_porq(node.right)

            if not contains_porq_l and not contains_porq_r:
                return False

            if contains_porq_l and contains_porq_r:
                ans = node

            return True

        contains_porq(root)

        return ans
