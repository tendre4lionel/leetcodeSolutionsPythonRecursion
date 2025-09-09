# 563 Binary Tree Tilt
# Algorithm:
# - Use iterative post-order traversal
# - For each node, compute left_sum and right_sum
# - Compute tilt as abs(left_sum - right_sum)
# - Maintain a dictionary to store subtree sums
# Complexity:
# - Time: O(n)
# - Space: O(n), stack + dictionary

"""
# Definition for a binary tree node:
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        stack = [(root, False)]
        node_sum = {}
        total_tilt = 0
        
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if visited:
                left_sum = node_sum.get(node.left, 0)
                right_sum = node_sum.get(node.right, 0)
                total_tilt += abs(left_sum - right_sum)
                node_sum[node] = node.val + left_sum + right_sum
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        
        return total_tilt


# Algorithm:
# - Use recursion to compute sum of subtree
# - Track total tilt in class-level state variable
# Complexity:
# - Time: O(n)
# - Space: O(h) recursion stack, h = height of tree

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total_tilt = 0
        
        def subtree_sum(node):
            if not node:
                return 0
            left = subtree_sum(node.left)
            right = subtree_sum(node.right)
            self.total_tilt += abs(left - right)
            return node.val + left + right
        
        subtree_sum(root)
        return self.total_tilt



# Algorithm:
# - Recursively compute (subtree_sum, subtree_tilt) for each node
# - Sum tilts of left, right, and current node
# Complexity:
# - Time: O(n)
# - Space: O(h) recursion stack

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if not node:
                return 0, 0  # subtree_sum, subtree_tilt
            left_sum, left_tilt = helper(node.left)
            right_sum, right_tilt = helper(node.right)
            tilt = abs(left_sum - right_sum)
            total_tilt = left_tilt + right_tilt + tilt
            return node.val + left_sum + right_sum, total_tilt
        
        _, total = helper(root)
        return total



