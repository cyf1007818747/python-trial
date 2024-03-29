# your original solution without any external reference
from typing import Optional


class TreeNodeOriginal:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# you write again after checking the official definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # copied from internet
    def __repr__(self, level=0):
        ret = "\t"*level + repr(self.val) + "\n"
        if self.left is not None:  # Check if the left child exists
            ret += self.left.__repr__(level+1)
        if self.right is not None:  # Check if the right child exists
            ret += self.right.__repr__(level+1)
        return ret
    
# typed version, but has some issues
# class TreeNodeTyped:
#     def __init__(self, val: int = 0, left: Optional[TreeNodeTyped]=None, right: Optional[TreeNodeTyped]=None):
#         self.val = val,
#         self.left = left
#         self.right = right
        
def treeTest():
    tree0 = TreeNode(1)
    tree0.left = TreeNode(10, TreeNode(100), TreeNode(101))
    tree0.right = TreeNode(11, TreeNode(110), TreeNode(111))
    print('tree0:\n', tree0)

        

treeTest()