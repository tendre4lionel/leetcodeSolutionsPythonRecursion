# 404 Sum of Left Leaves
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # Recursive helper function
        def dfs(node, is_left):
            """
            node: current TreeNode
            is_left: boolean indicating if node is a left child
            """
            # Base case: empty node
            if not node:
                return 0

            # Check if node is a leaf
            if not node.left and not node.right:
                # Only count it if it is a left leaf
                return node.val if is_left else 0

            # Recurse on left and right children
            left_sum = dfs(node.left, True)   # left child marked as left
            right_sum = dfs(node.right, False) # right child marked as not left

            return left_sum + right_sum

        # Start recursion from root (root itself is not a left child)
        return dfs(root, False)
