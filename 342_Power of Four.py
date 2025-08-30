# 342 Power of Four
class Solution(object):
    def isPowerOfFour(self, n):
        """
        Check recursively if n is a power of four.
        
        :type n: int
        :rtype: bool
        """
        # Base case: 4^0 = 1
        if n == 1:
            return True
        
        # Base case: n <= 0 cannot be power of 4
        if n <= 0:
            return False
        
        # If divisible by 4, check recursively n // 4
        if n % 4 == 0:
            return self.isPowerOfFour(n // 4)
        else:
            # Not divisible by 4 → cannot be power of 4
            return False
