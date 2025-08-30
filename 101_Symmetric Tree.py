# 101 Symmetric Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        Recursive solution to check if a binary tree is symmetric.

        Problem:
        - A tree is symmetric if its left and right subtrees are mirrors of each other.

        Approach (Recursive):
        - Define a helper function isMirror(t1, t2) that checks if two trees are mirror images.
        - Base cases:
            1. Both t1 and t2 are None → symmetric at this level → return True
            2. One is None, the other isn't → not symmetric → return False
            3. Values differ → not symmetric → return False
        - Recursive case:
            - Left subtree of t1 vs Right subtree of t2
            - Right subtree of t1 vs Left subtree of t2
        """

        def isMirror(t1, t2):
            # Both nodes are None → symmetric
            if not t1 and not t2:
                return True
            # One node is None → not symmetric
            if not t1 or not t2:
                return False
            # Values differ → not symmetric
            if t1.val != t2.val:
                return False
            # Recursively check mirror symmetry of subtrees
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        # Empty tree is symmetric
        if not root:
            return True

        # Start by comparing left and right subtrees of root
        return isMirror(root.left, root.right)


# ---------------- Example Usage ----------------
# Symmetric Tree:
#      1
#     / \
#    2   2
#   / \ / \
#  3  4 4  3

root = TreeNode(1,
                TreeNode(2, TreeNode(3), TreeNode(4)),
                TreeNode(2, TreeNode(4), TreeNode(3)))

sol = Solution()
print(sol.isSymmetric(root))  # Output: True
