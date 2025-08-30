# 257 Binary Tree Paths
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        Return all root-to-leaf paths of a binary tree recursively.
        """

        # List to store all the paths found
        paths = []

        # Helper function: recursive DFS (Depth First Search) to explore the tree
        def dfs(node, path):
            # Base case: if the node is None, return
            if node is None:
                return

            # If path is empty (first node), just start with the node's value
            # If path is not empty, add the current node's value to the existing path
            if path == "":
                new_path = str(node.val)  # Start path with the root node
            else:
                new_path = path + "->" + str(node.val)  # Append current node value to the path

            # Check if the current node is a leaf (no left and right child)
            if node.left is None and node.right is None:
                # If it's a leaf, add the path to the result list
                paths.append(new_path)
                return  # Stop further recursion down this path

            # Recursively explore the left subtree if it exists
            # Continue with the updated path for left child
            dfs(node.left, new_path)
            
            # Recursively explore the right subtree if it exists
            # Continue with the updated path for right child
            dfs(node.right, new_path)

        # Start DFS from the root with an empty path
        dfs(root, "")

        # Return the list of all paths found
        return paths


