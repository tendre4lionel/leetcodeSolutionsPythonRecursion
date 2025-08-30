# 234 Palindrome Linked List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        Recursively check if a singly linked list is a palindrome.
        Time: O(n), Space: O(n) for recursion stack
        """

        # Pointer to traverse from the front
        self.front_pointer = head

        def recursively_check(current):
            # Base case: reached end of the list
            if current is None:
                return True

            # Recurse to next node
            # If any deeper recursion returns False, stop immediately and propagate False upward.
            if not recursively_check(current.next):
                return False

            # Compare current node from back with front_pointer
            if current.val != self.front_pointer.val:
                return False

            # Move front_pointer forward
            self.front_pointer = self.front_pointer.next

            return True

        return recursively_check(head)



