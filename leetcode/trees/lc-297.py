"""
Serialize and deserialize binary tree
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# traverse by layer / bfs
# start to AC - 18:34
# AC
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"

        rtn = ""
        q = [root]

        while q:
            front = q.pop(0)
            if front:
                rtn += str(front.val) + ","
            else:
                rtn += "None"+","
                continue
            q.append(front.left)
            q.append(front.right)
        
        # print('rtn:', rtn)
        
        return rtn[:-1]
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "None":
            return None
        
        datalist = data.split(",")
        root = TreeNode(int(datalist[0]))
        q = [root]
        i = 1
        while q:
            # // front = q.pop()
            front = q.pop(0)
            if datalist[i] != "None":
                front.left = TreeNode(int(datalist[i]))
                q.append(front.left)
            i += 1
            if datalist[i] != "None":
                front.right = TreeNode(int(datalist[i]))
                q.append(front.right)
            i += 1

        return root
