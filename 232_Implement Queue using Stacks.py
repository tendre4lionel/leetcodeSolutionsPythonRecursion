# 232 Implement Queue using Stacks
class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        We use two stacks:
        1. stack_in: for push operations (new elements enter here)
        2. stack_out: for pop/peek operations (elements to be dequeued)
        """
        self.stack_in = []   # Stack to store new elements
        self.stack_out = []  # Stack to store elements in correct dequeue order

    def push(self, x):
        """
        Push element x to the back of queue.
        Simply push it to stack_in.
        """
        self.stack_in.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns it.
        If stack_out is empty, pour all elements from stack_in to stack_out
        to reverse the order (so the oldest element is on top of stack_out).
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # Pop from stack_out which is the front of the queue
        return self.stack_out.pop()

    def peek(self):
        """
        Get the front element.
        If stack_out is empty, pour all elements from stack_in to stack_out.
        Then peek at the top of stack_out.
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]  # Peek top element without popping

    def empty(self):
        """
        Returns whether the queue is empty.
        Queue is empty if both stacks are empty.
        """
        return not self.stack_in and not self.stack_out


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
