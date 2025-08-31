# 441 Arranging Coins
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        # recursive helper function
        def helper(remaining, row):
            # Base case: if not enough coins for the next row, stop
            if remaining < row:
                return row - 1  # last complete row

            # Recursive step: use `row` coins and move to next row
            return helper(remaining - row, row + 1)

        # Start recursion with row 1
        return helper(n, 1)
"""
3. Math Formula (O(1))
Solve quadratic inequality: isolate k
k^2+k≤2n
Using quadratic formula:
Take floor:
k=(-1+sqrt(1+8n))/2

import math

class Solution(object):
    def arrangeCoins(self, n):
        return int((math.sqrt(1 + 8*n) - 1) // 2)
"""