
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# start to AC: 8:06
# GOOD !!!!! one time pass without any bug and rework 
# AC
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stk = []
        good_nodes = 0

        def dfs(node: TreeNode):
            if not node:
                return
            
            nonlocal stk, good_nodes

            if not stk:
                stk.append(node.val)
                good_nodes += 1
            else:
                prev_max = stk[-1]
                if node.val >= prev_max:
                    stk.append(node.val)
                    good_nodes += 1
                else:
                    stk.append(prev_max)

            dfs(node.left)
            dfs(node.right)

            stk.pop()

        dfs(root)

        return good_nodes
    
# use parameter passing with nonlocal good_nodes
# start to AC: 3:08
# AC
class Solution2:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        def dfs(node: TreeNode, prev_max: int):
            if not node:
                return

            nonlocal good_nodes

            if node.val >= prev_max:
                good_nodes += 1
                prev_max = node.val

            # be careful !! 
            # // dfs(node.left, node.val) 
            # // dfs(node.right, node.val)
            dfs(node.left, prev_max)
            dfs(node.right, prev_max)

        dfs(root, float('-inf'))

        return good_nodes
    

# use parameter passing without nonlocal variable
# little bit harder to understand than solution 2
# recommend solutino2 in real interview
# start to AC: 2:41
# AC
class Solution3:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, prev_max: int) -> int:
            if not node:
                return 0

            good_nodes = 0
            if node.val >= prev_max:
                good_nodes += 1
                prev_max = node.val
            
            good_nodes += dfs(node.left, prev_max) + dfs(node.right, prev_max)
            
            return good_nodes

        return dfs(root, float('-inf'))
