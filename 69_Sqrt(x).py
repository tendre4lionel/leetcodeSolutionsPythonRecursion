class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        # Recursive helper for binary search
        def binary_search(left, right):
            # Base case: when left > right, return the last valid candidate
            if left > right:
                return right  # 'right' is the floor of sqrt(x)

            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid  # exact square root found
            elif square < x:
                # mid is too small, search in right half
                return binary_search(mid + 1, right)
            else:
                # mid is too large, search in left half
                return binary_search(left, mid - 1)

        # Edge case: sqrt(0) = 0
        if x == 0:
            return 0

        # Start recursion between 1 and x//2 + 1
        return binary_search(1, x // 2 + 1)
