# 203 Remove Linked List Elements
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if not head:  # Base case: empty list
            return None
        
        # Recursively remove elements from the rest of the list
        head.next = self.removeElements(head.next, val)
        
        # If current node's value equals val, skip it
        if head.val == val:
            return head.next
        else:
            return head

