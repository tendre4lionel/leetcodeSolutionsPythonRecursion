# 108 Convert Sorted Array to Binary Search Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        Recursive solution to convert a sorted array into a height-balanced BST.

        Problem:
        - Input: sorted array in ascending order.
        - Output: height-balanced BST.
        - Height-balanced: difference of heights of left and right subtrees
          of every node is at most 1.

        Approach (Recursive):
        --------------------
        - Use the middle element as the root (ensures balanced tree).
        - Recursively build:
            1. Left subtree from left half of array.
            2. Right subtree from right half of array.
        - Base case:
            - If subarray is empty → return None.
        """

        # Base case: empty array → no node
        if not nums:
            return None

        # Middle index
        mid = len(nums) // 2

        # Create root node with middle element
        root = TreeNode(nums[mid])

        # Recursively build left subtree
        root.left = self.sortedArrayToBST(nums[:mid])

        # Recursively build right subtree
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root


# ---------------- Example Usage ----------------
# Sorted array
nums = [-10, -3, 0, 5, 9]

sol = Solution()
bst_root = sol.sortedArrayToBST(nums)

# Helper function to do inorder traversal (should return sorted array)
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

print(inorder(bst_root))  # Output: [-10, -3, 0, 5, 9]
