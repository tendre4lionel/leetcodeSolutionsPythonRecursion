# 145 Binary Tree Postorder Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        Recursive solution for postorder traversal of a binary tree.

        Problem:
        - Postorder traversal: visit nodes in the order:
            1. Left subtree
            2. Right subtree
            3. Current node

        Approach (Recursive):
        --------------------
        1. Base case: if the current node is None, return an empty list.
        2. Recursively traverse the left subtree
        3. Recursively traverse the right subtree
        4. Visit the current node (include root.val)
        5. Combine left + right + current value and return
        """

        # Base case: empty node
        if root is None:
            return []

        # Step 1: Traverse left subtree recursively
        left_values = self.postorderTraversal(root.left)

        # Step 2: Traverse right subtree recursively
        right_values = self.postorderTraversal(root.right)

        # Step 3: Visit current node
        current_value = [root.val]

        # Combine results: left + right + current node
        return left_values + right_values + current_value


# ---------------- Example Usage ----------------
# Tree:
#      1
#       \
#        2
#       /
#      3

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
print(sol.postorderTraversal(root))  # Output: [3, 2, 1]
