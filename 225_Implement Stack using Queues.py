# 225 Implement Stack using Queues
from collections import deque

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        We use two queues:
        - q1: main queue that always has the "top" element at the front
        - q2: temporary queue used during push operation
        """
        self.q1 = deque()  # main queue
        self.q2 = deque()  # temporary queue

    def push(self, x):
        """
        Push element x onto stack.
        Steps:
        1. Add x to the temporary queue q2.
        2. Move all elements from q1 to q2, so the newest element is at the front.
        3. Swap q1 and q2, making q1 the main queue with correct order.
        :type x: int
        :rtype: None
        """
        self.q2.append(x)  # Step 1: add new element to q2
        
        # Step 2: move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        # Step 3: swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """
        Removes the element on top of the stack and returns it.
        Since the top is always at the front of q1, just pop from left.
        :rtype: int
        """
        return self.q1.popleft()

    def top(self):
        """
        Get the top element of the stack.
        The top element is always at the front of q1.
        :rtype: int
        """
        return self.q1[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.q1
 


 