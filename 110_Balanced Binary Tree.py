# 110 Balanced Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        Recursive solution to check if a binary tree is height-balanced.

        Problem:
        - A binary tree is height-balanced if:
            For every node, the difference between the heights of
            left and right subtrees is at most 1.

        Approach (Recursive):
        --------------------
        - Define a helper function that returns two things:
            1. Whether the subtree is balanced
            2. Its height
        - Base case:
            - If node is None → balanced, height = 0
        - Recursive case:
            - Check left subtree → get (is_left_balanced, left_height)
            - Check right subtree → get (is_right_balanced, right_height)
            - Current node is balanced if:
                a) left and right subtrees are balanced
                b) abs(left_height - right_height) <= 1
            - Height of current node = max(left_height, right_height) + 1
        """

        def helper(node):
            if not node:
                return True, 0  # Empty subtree: balanced, height=0

            # Recursively check left subtree
            left_balanced, left_height = helper(node.left)

            # Recursively check right subtree
            right_balanced, right_height = helper(node.right)

            # Current node balanced?
            current_balanced = (
                left_balanced and
                right_balanced and
                abs(left_height - right_height) <= 1
            )

            # Height of current node
            current_height = max(left_height, right_height) + 1

            return current_balanced, current_height

        balanced, _ = helper(root)
        return balanced


# ---------------- Example Usage ----------------
# Tree:
#      1
#     / \
#    2   2
#   / \
#  3   3
# / \
#4   4

root = TreeNode(1,
                TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
                TreeNode(2))

sol = Solution()
print(sol.isBalanced(root))  # Output: False
