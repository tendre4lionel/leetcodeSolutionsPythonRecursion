# 222 Count Complete Tree Nodes
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Base case: empty tree
        if not root:
            return 0
        
        # Helper to compute height recursively
        def leftHeight(node):
            if not node:
                return 0
            return 1 + leftHeight(node.left)
        
        def rightHeight(node):
            if not node:
                return 0
            return 1 + rightHeight(node.right)
        
        hl = leftHeight(root)
        hr = rightHeight(root)
        
        # If perfect tree
        if hl == hr:
            return 2 ** hl - 1
        
        # Otherwise, recursively count left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
