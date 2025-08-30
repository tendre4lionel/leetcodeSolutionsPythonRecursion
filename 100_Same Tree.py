# 100 Same Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        Recursive solution to check if two binary trees are the same.

        Problem:
        - Two trees are the same if:
            1. They are structurally identical.
            2. Nodes have the same values.

        Approach (Recursive):
        --------------------
        - Base case 1: if both nodes are None → trees match here → return True
        - Base case 2: if one node is None but the other isn't → trees differ → return False
        - Base case 3: if node values differ → return False
        - Recursive case:
            - Check if left subtrees are the same
            - Check if right subtrees are the same
            - Return True only if both subtrees match
        """

        # Case 1: both nodes are None → identical
        if not p and not q:
            return True

        # Case 2: one is None, the other isn't → not identical
        if not p or not q:
            return False

        # Case 3: values differ → not identical
        if p.val != q.val:
            return False

        # Recursive check for left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# ---------------- Example Usage ----------------
# Tree 1:      1         Tree 2:      1
#             / \                   / \
#            2   3                 2   3

p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))

sol = Solution()
print(sol.isSameTree(p, q))  # Output: True
