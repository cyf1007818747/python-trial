from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# preorder traversal of a tree using stack
def dfs_with_stack(root) -> List[int]:
    preorder_result = []

    if not root:
        return

    stack = [root]  # Initialize stack with root node

    while stack:
        current = stack.pop()  # Visit the top node
        preorder_result.append(current.val)  # Process the node

        # Push children of the visited node to the stack
        # Note: Right child is pushed first so that left child is processed first
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)


# inorder traversal of a tree using stack
def inorder_traversal(root: TreeNode) -> List[int]:
    stack = []
    current = root
    inorder_result = []

    while current is not None or stack:
        # Reach the leftmost node of the current node
        while current is not None:
            stack.append(current)
            current = current.left
        
        # Current must be None at this point
        current = stack.pop()
        inorder_result.append(current.val)   # Process the node's value

        # We have visited the node and its left subtree.
        # Now, it's right subtree's turn
        current = current.right

    return inorder_result

