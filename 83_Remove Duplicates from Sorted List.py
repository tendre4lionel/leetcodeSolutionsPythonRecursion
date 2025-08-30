# 83 Remove Duplicates from Sorted List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        Recursive solution to remove duplicates from a sorted linked list.

        Key Idea:
        - Since the list is sorted, duplicates must appear consecutively.
        - Process the list recursively, starting from the tail.
        - On the way back (unwinding recursion), check if the current node
          is a duplicate of its next node:
            - If yes → skip the current node.
            - If no  → keep the current node.
        """

        # Base case: if list is empty OR has only one node → return as is
        if not head or not head.next:
            return head

        # Step 1: Recursively deduplicate the rest of the list
        head.next = self.deleteDuplicates(head.next)

        # Step 2: Now compare current node with the (already deduplicated) next node
        if head.val == head.next.val:
            # Duplicate found → skip current node
            return head.next
        else:
            # No duplicate → keep current node
            return head
