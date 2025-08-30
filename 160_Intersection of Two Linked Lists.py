# 160 Intersection of Two Linked Lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        Recursive solution to find the intersection of two singly linked lists.

        Approach:
        1. Find the lengths of both lists recursively.
        2. Align the heads so that they have the same remaining length.
        3. Recursively traverse both lists in parallel:
            - If nodes are the same → intersection found
            - If either node is None → no intersection
        """

        # Helper to compute length recursively
        def getLength(node):
            if not node:
                return 0
            return 1 + getLength(node.next)

        # Helper to advance a list by n nodes
        def advance(node, n):
            if n == 0:
                return node
            return advance(node.next, n - 1)

        # Helper to find intersection recursively
        def findIntersection(nodeA, nodeB):
            if not nodeA or not nodeB:
                return None
            if nodeA == nodeB:
                return nodeA
            return findIntersection(nodeA.next, nodeB.next)

        lenA = getLength(headA)
        lenB = getLength(headB)

        # Align heads
        if lenA > lenB:
            headA = advance(headA, lenA - lenB)
        else:
            headB = advance(headB, lenB - lenA)

        # Recursively find intersection
        return findIntersection(headA, headB)


# ---------------- Example Usage ----------------
# List A: 4 -> 1 -> 8 -> 4 -> 5
# List B: 5 -> 0 -> 1 -> 8 -> 4 -> 5
# Intersection at node with value 8

a1 = ListNode(4)
a2 = ListNode(1)
b1 = ListNode(5)
b2 = ListNode(0)
b3 = ListNode(1)
c1 = ListNode(8)
c2 = ListNode(4)
c3 = ListNode(5)

# Connect lists
a1.next = a2
a2.next = c1
b1.next = b2
b2.next = b3
b3.next = c1
c1.next = c2
c2.next = c3

sol = Solution()
intersection = sol.getIntersectionNode(a1, b1)
print(intersection.val if intersection else None)  # Output: 8
