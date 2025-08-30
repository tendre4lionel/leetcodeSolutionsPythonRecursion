# 111 Minimum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        Recursive solution to find the minimum depth of a binary tree.

        Problem:
        - Minimum depth = number of nodes along the shortest path
          from root to the nearest leaf node.
        - A leaf node has no children.

        Approach (Recursive):
        --------------------
        - Base case: if root is None → depth = 0
        - If one of the subtrees is None, we cannot consider its depth
          because leaf must exist → only take the depth of the non-None subtree
        - If both subtrees exist → take min(left_depth, right_depth)
        - Add 1 to include current node
        """

        # Base case: empty node
        if not root:
            return 0

        # Leaf node: no children → depth = 1
        if not root.left and not root.right:
            return 1

        # If left child is None, recurse on right subtree only
        if not root.left:
            return self.minDepth(root.right) + 1

        # If right child is None, recurse on left subtree only
        if not root.right:
            return self.minDepth(root.left) + 1

        # If both children exist, take minimum of left and right depths
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# ---------------- Example Usage ----------------
# Tree:
#      1
#     / \
#    2   3
#   / 
#  4  

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))

sol = Solution()
print(sol.minDepth(root))  # Output: 2 (path 1 -> 3)
