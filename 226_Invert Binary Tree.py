# 226 Invert Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        Recursively inverts a binary tree.
        
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Base case: if the current node is None (empty), just return None
        # This handles leaf nodes' children automatically
        if root is None:
            return None
        
        # Print current node's value for debugging (optional)
        # print(f"Inverting node with value: {root.val}")
        
        # Recursively invert the left subtree
        left_inverted = self.invertTree(root.left)
        
        # Recursively invert the right subtree
        right_inverted = self.invertTree(root.right)
        
        # Swap the left and right children of the current node
        # This is what actually "inverts" the tree
        root.left = right_inverted
        root.right = left_inverted
        
        # Return the current node, which now has its children inverted
        return root
