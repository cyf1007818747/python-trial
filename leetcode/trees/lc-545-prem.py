# all copied from GPT since premium
from typing import List

"""
LeetCode Problem 545, "Boundary of Binary Tree," asks you to return the values of the nodes forming the 
boundary of a binary tree in an anti-clockwise direction starting from the root. The boundary includes 
the left boundary, leaves, and right boundary in order without duplicate nodes. The left boundary is 
defined as the path from the root to the left-most node. The right boundary is the path from the root 
to the right-most node. The leaves are all the leaf nodes of the tree, excluding the root if it is a leaf.

To solve this problem, we can divide it into three main parts:

Left Boundary (excluding the leaf node): Traverse from the root to the left-most node, adding nodes to the 
boundary list. Skip leaf nodes and ensure not to include the last node if it's a leaf.
Leaves: Perform a depth-first search (DFS) or breadth-first search (BFS) to find and add all leaf nodes 
from left to right.

Right Boundary (excluding the leaf node): Traverse from the root to the right-most node, adding nodes to a 
temporary list. Reverse this list and add it to the boundary list at the end to ensure correct order. Skip 
leaf nodes and ensure not to include the last node if it's a leaf.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        # Function to check if a node is a leaf
        # this is when you would like to write a helper function # *
        def is_leaf(node):
            return node.left is None and node.right is None
        
        # Function to add left boundary excluding leaf nodes
        def add_left_boundary(node):
            if node and not is_leaf(node):
                boundary.append(node.val)
                if node.left:
                    add_left_boundary(node.left)
                else:
                    add_left_boundary(node.right)
        
        # Function to add leaf nodes
        def add_leaves(node):
            if node:
                if is_leaf(node):
                    boundary.append(node.val)
                else:
                    add_leaves(node.left)
                    add_leaves(node.right)
        
        # Function to add right boundary excluding leaf nodes
        def add_right_boundary(node):
            if node and not is_leaf(node):
                if node.right:
                    add_right_boundary(node.right)
                else:
                    add_right_boundary(node.left)
                boundary.append(node.val)  # Add after child visit to reverse order # *
        
        boundary = []
        if not is_leaf(root): # *
            boundary.append(root.val)
        add_left_boundary(root.left)
        add_leaves(root)
        add_right_boundary(root.right)
        
        return boundary
