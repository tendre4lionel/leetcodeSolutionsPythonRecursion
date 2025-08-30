# 94 Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        Recursive solution for inorder traversal of a binary tree.

        Problem:
        - Inorder traversal: visit nodes in the order:
            1. Left subtree
            2. Current node
            3. Right subtree

        Approach (Recursive):
        --------------------
        1. Base case: if the current node is None, return an empty list.
        2. Recursively traverse the left subtree and collect values.
        3. Add the current node's value.
        4. Recursively traverse the right subtree and collect values.
        5. Combine left, current, and right values and return.
        """

        # Base case: empty node
        if root is None:
            return []

        # Step 1: Traverse left subtree
        left_values = self.inorderTraversal(root.left)

        # Step 2: Visit current node
        current_value = [root.val]

        # Step 3: Traverse right subtree
        right_values = self.inorderTraversal(root.right)

        # Combine results
        return left_values + current_value + right_values


# ---------------- Example Usage ----------------
# Building the tree:
#      1
#       \
#        2
#       /
#      3

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
print(sol.inorderTraversal(root))  # Output: [1, 3, 2]
