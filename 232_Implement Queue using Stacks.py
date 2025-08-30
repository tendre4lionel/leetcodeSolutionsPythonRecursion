# 232 Implement Queue using Stacks
class MyQueue(object):
    def __init__(self):
        # Initialize two stacks
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        """
        Push element x to the back of the queue.
        """
        # Always push to in_stack
        self.in_stack.append(x)

    def pop(self):
        """
        Removes the element from the front of the queue and returns it.
        """
        # If out_stack is empty, move all elements from in_stack to out_stack
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        # Pop from out_stack (this gives us the front of the queue)
        return self.out_stack.pop()

    def peek(self):
        """
        Get the front element.
        """
        # If out_stack is empty, move all elements from in_stack to out_stack
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        # Peek from out_stack (this gives us the front of the queue)
        return self.out_stack[-1]

    def empty(self):
        """
        Return whether the queue is empty.
        """
        # Queue is empty if both in_stack and out_stack are empty
        return not self.in_stack and not self.out_stack


# ---------------- Example Usage ----------------
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())  # Output: 1
print(queue.pop())   # Output: 1
print(queue.empty()) # Output: False
queue.push(3)
print(queue.pop())   # Output: 2
print(queue.pop())   # Output: 3
print(queue.empty()) # Output: True
