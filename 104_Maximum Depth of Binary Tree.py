# 104 Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        Recursive solution to find the maximum depth of a binary tree.

        Problem:
        - Maximum depth = number of nodes along the longest path
          from the root down to the farthest leaf node.

        Approach (Recursive):
        --------------------
        1. Base case: if the node is None → depth is 0.
        2. Recursive case:
            - Compute max depth of left subtree.
            - Compute max depth of right subtree.
            - The depth at current node = max(left, right) + 1
              (+1 for the current node itself)
        """

        # Base case: empty node contributes 0 to depth
        if not root:
            return 0

        # Recursively find depth of left subtree
        left_depth = self.maxDepth(root.left)

        # Recursively find depth of right subtree
        right_depth = self.maxDepth(root.right)

        # Depth at current node = max of left and right + 1
        return max(left_depth, right_depth) + 1


# ---------------- Example Usage ----------------
# Tree:
#      1
#     / \
#    2   3
#   / \
#  4   5

root = TreeNode(1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3))

sol = Solution()
print(sol.maxDepth(root))  # Output: 3
