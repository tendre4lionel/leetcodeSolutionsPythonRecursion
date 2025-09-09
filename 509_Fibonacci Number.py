# 509 Fibonacci Number
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Algorithm (Iterative DP):
        # 1. Handle base cases: F(0)=0, F(1)=1.
        # 2. Use two variables to store last two Fibonacci numbers.
        # 3. Iteratively compute up to F(n).
        #
        # Time Complexity: O(n)   (one loop up to n)
        # Space Complexity: O(1)  (constant memory)

        if n == 0:
            return 0
        if n == 1:
            return 1

        prev2 = 0  # F(0)
        prev1 = 1  # F(1)

        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Algorithm (Recursive with memoization state):
        # 1. Use recursion to compute Fibonacci.
        # 2. Store results in a shared dictionary to avoid recomputation.
        # 3. Base cases: F(0)=0, F(1)=1.
        #
        # Time Complexity: O(n)   (each number computed once)
        # Space Complexity: O(n)  (recursion depth + memo dictionary)

        memo = {0: 0, 1: 1}  # shared state

        def helper(k):
            if k in memo:
                return memo[k]
            memo[k] = helper(k - 1) + helper(k - 2)
            return memo[k]

        return helper(n)

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Algorithm (Pure recursion):
        # 1. Define fib(n) = fib(n-1) + fib(n-2).
        # 2. Base cases: F(0)=0, F(1)=1.
        # 3. No memoization, so exponential calls.
        #
        # Time Complexity: O(2^n)   (recomputes many subproblems)
        # Space Complexity: O(n)    (recursion depth)

        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


