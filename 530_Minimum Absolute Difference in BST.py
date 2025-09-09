# 530 Minimum Absolute Difference in BST
# Algorithm:
# - Perform iterative in-order traversal of BST using a stack
# - Keep track of previous node value to compute differences
# - Update minimum difference when a smaller difference is found
# Complexity:
# - Time: O(n), where n = number of nodes (each node visited once)
# - Space: O(h), where h = height of BST (stack stores nodes along the path)

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        current = root
        prev = None  # previous node value
        min_diff = float('inf')
        
        while stack or current:
            # go as left as possible
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            
            # compute difference with previous node
            if prev is not None:
                min_diff = min(min_diff, current.val - prev)
            prev = current.val
            
            current = current.right
        
        return min_diff


# Algorithm:
# - Perform recursive in-order traversal
# - Use state variables: prev (previous node) and min_diff (minimum difference)
# - Update min_diff at each step
# Complexity:
# - Time: O(n), each node visited once
# - Space: O(h), recursion stack where h = height of BST

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = None       # state: previous node value
        self.min_diff = float('inf')  # state: minimum difference
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
        
        inorder(root)
        return self.min_diff



# Algorithm:
# - Perform recursive in-order traversal
# - Pass previous node value and minimum difference as parameters
# - Return the updated min_diff
# Complexity:
# - Time: O(n)
# - Space: O(h) recursion stack

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(node, prev, min_diff):
            if not node:
                return prev, min_diff
            
            # traverse left
            prev, min_diff = inorder(node.left, prev, min_diff)
            
            # update min_diff
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val
            
            # traverse right
            prev, min_diff = inorder(node.right, prev, min_diff)
            return prev, min_diff
        
        _, result = inorder(root, None, float('inf'))
        return result




