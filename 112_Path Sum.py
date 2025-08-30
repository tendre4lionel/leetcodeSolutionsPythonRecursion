# 112 Path Sum
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        Recursive solution to check if there exists a root-to-leaf path
        whose node values sum up to targetSum.

        Approach (Recursive):
        --------------------
        - Base case 1: if root is None → no path → return False
        - Base case 2: if root is a leaf (no children):
            - Check if root.val == targetSum → return True or False
        - Recursive case:
            - Subtract root.val from targetSum
            - Recurse on left and right subtrees with updated targetSum
            - Return True if any subtree has a valid path
        """

        if not root:
            return False

        # Check if we are at a leaf node
        if not root.left and not root.right:
            return root.val == targetSum

        # Update remaining sum
        remaining_sum = targetSum - root.val

        # Recurse on left and right subtrees
        return (self.hasPathSum(root.left, remaining_sum) or
                self.hasPathSum(root.right, remaining_sum))


# ---------------- Example Usage ----------------
# Tree:
#      5
#     / \
#    4   8
#   /   / \
#  11  13  4
# /  \       \
#7    2       1

root = TreeNode(5,
                TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))

targetSum = 22

sol = Solution()
print(sol.hasPathSum(root, targetSum))  # Output: True (path 5->4->11->2)
