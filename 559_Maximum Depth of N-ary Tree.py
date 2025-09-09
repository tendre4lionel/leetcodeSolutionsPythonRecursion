# 559 Maximum Depth of N-ary Tree

# Algorithm:
# - Use a queue to perform level-order traversal (BFS)
# - Increment depth at each level
# Complexity:
# - Time: O(n), n = number of nodes
# - Space: O(n), for the queue

"""
# Definition for a Node (for reference)
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

from collections import deque

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
            depth += 1
        
        return depth


# Algorithm:
# - Use DFS recursively
# - Track current depth as state (optional, but here we compute max among children)
# Complexity:
# - Time: O(n), each node visited once
# - Space: O(h), recursion stack, h = height of tree

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        
        def dfs(node):
            if not node.children:
                return 1
            max_child_depth = 0
            for child in node.children:
                max_child_depth = max(max_child_depth, dfs(child))
            return 1 + max_child_depth
        
        return dfs(root)




# Algorithm:
# - For each node, return 1 + max(depth of children)
# - Base case: node is None → depth 0
# Complexity:
# - Time: O(n)
# - Space: O(h) recursion stack

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max([self.maxDepth(child) for child in root.children] + [0])

# Explanation:
# - The `[0]` ensures that if there are no children, max returns 0
# - Then 1 + 0 = 1, which is correct for leaf nodes







