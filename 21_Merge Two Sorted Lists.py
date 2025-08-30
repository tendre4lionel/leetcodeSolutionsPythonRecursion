# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        Fully recursive solution to merge two sorted linked lists.
        """

        # Base case: if one list is empty, return the other
        if not list1:
            return list2
        if not list2:
            return list1

        # Compare the current nodes of both lists
        if list1.val <= list2.val:
            # list1 node is smaller or equal, it will be the next node in merged list
            # Recursively merge the rest of list1 with list2
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # list2 node is smaller, it will be the next node in merged list
            # Recursively merge list1 with the rest of list2
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
