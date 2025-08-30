# 144 Binary Tree Preorder Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        Recursive solution for preorder traversal of a binary tree.

        Problem:
        - Preorder traversal: visit nodes in the order:
            1. Current node
            2. Left subtree
            3. Right subtree

        Approach (Recursive):
        --------------------
        1. Base case: if the current node is None, return an empty list.
        2. Visit the current node: include root.val
        3. Recursively traverse the left subtree
        4. Recursively traverse the right subtree
        5. Combine current value + left + right and return
        """

        # Base case: empty node
        if root is None:
            return []

        # Step 1: Visit current node
        current_value = [root.val]

        # Step 2: Traverse left subtree recursively
        left_values = self.preorderTraversal(root.left)

        # Step 3: Traverse right subtree recursively
        right_values = self.preorderTraversal(root.right)

        # Combine results: current node first, then left, then right
        return current_value + left_values + right_values


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
print(sol.preorderTraversal(root))  # Output: [1, 2, 3]
