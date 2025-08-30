# 141 Linked List Cycle
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def hasCycle(self, head):
        """
        Recursive solution to detect a cycle in a linked list using a set.

        Approach:
        - Keep a set of visited nodes.
        - Base case: if current node is None → no cycle → return False
        - If node is in visited set → cycle detected → return True
        - Otherwise, add node to set and recurse on next node
        """

        visited = set()

        def helper(node):
            if not node:
                return False
            if node in visited:
                return True
            visited.add(node)
            return helper(node.next)

        return helper(head)


# ---------------- Example Usage ----------------
# Creating a cycle: 3 -> 2 -> 0 -> -4 -> 2 ...
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # cycle here

sol = Solution()
print(sol.hasCycle(node1))  # Output: True
