# 206 Reverse Linked List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Base case: empty list or last node
        if not head or not head.next:
            return head
        
        # Recursively reverse the rest of the list
        new_head = self.reverseList(head.next)
        
        # Reverse the link
        head.next.next = head
        head.next = None
        
        return new_head
