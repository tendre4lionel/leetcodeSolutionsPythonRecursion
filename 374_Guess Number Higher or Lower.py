# 374 Guess Number Higher or Lower
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Recursive helper function using binary search
        def helper(low, high):
            # Base case: low exceeds high (should not happen normally)
            if low > high:
                return -1  # safety

            # Pick the middle number
            mid = (low + high) // 2

            # Use the guess API
            res = guess(mid)

            if res == 0:
                # Found the picked number
                return mid
            elif res == 1:
                # Pick is higher than mid → search upper half
                return helper(mid + 1, high)
            else:
                # Pick is lower than mid → search lower half
                return helper(low, mid - 1)

        # Start recursion with full range [1, n]
        return helper(1, n)
