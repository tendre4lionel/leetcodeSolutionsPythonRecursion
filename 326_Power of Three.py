# 326 Power of Three
class Solution(object):
    def isPowerOfThree(self, n):
        """
        Check if n is a power of three using recursion.
        
        :type n: int
        :rtype: bool
        """
        # Base case: 1 is 3^0
        if n == 1:
            return True
        
        # Base case: 0 or negative numbers cannot be powers of 3
        if n <= 0:
            return False
        
        # If n is divisible by 3, check recursively for n / 3
        if n % 3 == 0:
            return self.isPowerOfThree(n // 3)
        else:
            # If not divisible by 3, it cannot be a power of 3
            return False
