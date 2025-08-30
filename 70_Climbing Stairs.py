class Solution(object):
    def climbStairs(self, n):
        """
        Pure recursive solution to Climbing Stairs (no memoization).

        Problem:
        - You can climb 1 or 2 steps at a time.
        - Count the number of distinct ways to reach the top (step n).

        Approach:
        - Let f(n) = number of ways to reach step n
        - f(n) = f(n-1) + f(n-2) (1-step or 2-step)
        - Base cases:
            f(0) = 1 (already at the bottom, one way: do nothing)
            f(1) = 1 (only one step possible)
        """

        # Base cases
        if n == 0:
            return 1  # Only one way to stay at ground level
        if n == 1:
            return 1  # Only one way to climb a single step

        # Recursive case: sum of ways from the previous 1 step and 2 steps
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# Example usage:
sol = Solution()
print(sol.climbStairs(5))  # Output: 8
