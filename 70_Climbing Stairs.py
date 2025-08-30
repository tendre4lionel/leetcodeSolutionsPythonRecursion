# 70 Climbing Stairs
def climbStairs(n: int) -> int:
    """
    Recursive solution to the Climbing Stairs problem.

    Problem Restated:
    - We need to reach the 'n-th' step.
    - At each step, we can climb either 1 step or 2 steps.
    - We want to count how many distinct sequences of steps 
      (made of 1s and 2s) will lead us to the top.

    Approach (Recursive):
    --------------------
    Let's say we are at step `n`.
    - If we take a "1 step" move → now we must solve the subproblem for `n-1`.
    - If we take a "2 steps" move → now we must solve the subproblem for `n-2`.
    
    So, the number of ways to reach step `n` is:
        climbStairs(n-1) + climbStairs(n-2)
    
    This is exactly the Fibonacci recurrence.

    Base Cases:
    -----------
    - If n == 0:
        There's 1 way to stay at the ground (do nothing).
    - If n == 1:
        There's only 1 way: take a single step.
    - If n == 2:
        There are 2 ways: (1+1) or (2).

    Note:
    -----
    This version is "pure recursive" (no memoization).
    It's very inefficient for large n (exponential runtime),
    but demonstrates the recursive idea clearly.
    """

    # Base case: no steps left → 1 valid way (do nothing)
    if n == 0:
        return 1
    
    # Base case: only one step left → only one way to take it
    if n == 1:
        return 1

    # Recursive case:
    # - If we take a single step, we need to solve for (n-1)
    # - If we take two steps, we need to solve for (n-2)
    return climbStairs(n-1) + climbStairs(n-2)


# Example usage:
print(climbStairs(5))  # Output: 8
