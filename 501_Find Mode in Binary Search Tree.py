# 501 Find Mode in Binary Search Tree
1️⃣ Iterative Solution
class Solution(object):
    def findMode_iterative(self, root):
        """
        Iterative approach using inorder traversal + hashmap.
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        # Stack for inorder traversal
        stack = []
        node = root

        # Dictionary to count frequency of values
        freq = {}

        # Inorder traversal loop
        while stack or node:
            # Go left as much as possible
            while node:
                stack.append(node)
                node = node.left

            # Visit node
            node = stack.pop()
            val = node.val

            # Count frequency of this value
            freq[val] = freq.get(val, 0) + 1

            # Go to right subtree
            node = node.right

        # Find maximum frequency
        max_freq = max(freq.values())

        # Collect all keys with max frequency
        result = [k for k, v in freq.items() if v == max_freq]
        return result

2️⃣ Recursive with State (Tracking Counts in Global Variables)
class Solution(object):
    def findMode_memoization(self, root):
        """
        Recursive inorder traversal with state (tracking counts).
        :type root: TreeNode
        :rtype: List[int]
        """

        # State variables stored in lists (mutable in recursion)
        self.prev_val = None  # last seen value
        self.curr_count = 0   # count for current value
        self.max_count = 0    # global max count
        self.modes = []       # result list

        def inorder(node):
            """Recursive inorder traversal with counting."""
            if not node:
                return

            # Left subtree
            inorder(node.left)

            # Process current node
            if self.prev_val == node.val:
                # Same value as before → increment count
                self.curr_count += 1
            else:
                # Different value → reset count
                self.curr_count = 1
                self.prev_val = node.val

            # Update modes list
            if self.curr_count > self.max_count:
                # Found new max → reset modes list
                self.max_count = self.curr_count
                self.modes = [node.val]
            elif self.curr_count == self.max_count:
                # Tie → append this value
                self.modes.append(node.val)

            # Right subtree
            inorder(node.right)

        # Run traversal
        inorder(root)
        return self.modes


3️⃣ Pure Recursion (Collect Values First, Then Count)
class Solution(object):
    def findMode_recursive(self, root):
        """
        Pure recursive solution: collect values, then compute mode.
        :type root: TreeNode
        :rtype: List[int]
        """

        def inorder(node):
            """Recursively collect values with inorder traversal."""
            if not node:
                return []
            # Concatenate left + root + right
            return inorder(node.left) + [node.val] + inorder(node.right)

        # Step 1: collect all values
        values = inorder(root)

        # Step 2: recursive function to count frequency
        def count_freq(arr, freq):
            if not arr:
                return freq
            head, tail = arr[0], arr[1:]
            freq[head] = freq.get(head, 0) + 1
            return count_freq(tail, freq)

        freq = count_freq(values, {})

        # Step 3: find maximum frequency
        def max_val(arr):
            if not arr:
                return 0
            return max(arr[0], max_val(arr[1:]))

        max_freq = max_val(freq.values())

        # Step 4: collect all keys with max frequency
        def collect_modes(items, maxf):
            if not items:
                return []
            (k, v), rest = items[0], items[1:]
            if v == maxf:
                return [k] + collect_modes(rest, maxf)
            return collect_modes(rest, maxf)

        return collect_modes(freq.items(), max_freq)













