# 543 Diameter of Binary Tree
# Algorithm:
# - Use iterative post-order traversal to compute heights of nodes
# - Track maximum diameter as the sum of left and right heights
# Complexity:
# - Time: O(n), n = number of nodes
# - Space: O(n), stack stores nodes during traversal

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        stack = [(root, False)]
        node_to_height = {}
        max_diameter = 0
        
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if visited:
                left_height = node_to_height.get(node.left, 0)
                right_height = node_to_height.get(node.right, 0)
                node_to_height[node] = 1 + max(left_height, right_height)
                max_diameter = max(max_diameter, left_height + right_height)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        
        return max_diameter






# Algorithm:
# - Use recursion to compute height of each node
# - Use class-level state variable to track maximum diameter
# Complexity:
# - Time: O(n), each node visited once
# - Space: O(h), recursion stack, h = height of tree

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diameter = 0  # state variable
        
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            # Update maximum diameter at this node
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.max_diameter



# Algorithm:
# - For each node, recursively compute:
#   (diameter in subtree, height of subtree)
# - Compute diameter including current node as left_height + right_height
# - Return max(diameter) and height to parent
# Complexity:
# - Time: O(n)
# - Space: O(h) recursion stack

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0, 0  # diameter, height
            
            left_dia, left_height = dfs(node.left)
            right_dia, right_height = dfs(node.right)
            
            # Diameter through current node
            curr_dia = left_height + right_height
            # Maximum diameter in the subtree
            max_dia = max(left_dia, right_dia, curr_dia)
            # Height of current node
            height = 1 + max(left_height, right_height)
            return max_dia, height
        
        diameter, _ = dfs(root)
        return diameter
