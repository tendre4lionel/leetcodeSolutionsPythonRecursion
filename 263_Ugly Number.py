# 263 Ugly Number
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Base case: n should be positive
        if n <= 0:
            return False
        
        # Base case: 1 is considered an ugly number
        if n == 1:
            return True
        
        # Recursively divide by 2, 3, or 5 if divisible
        if n % 2 == 0:
            return self.isUgly(n // 2)
        if n % 3 == 0:
            return self.isUgly(n // 3)
        if n % 5 == 0:
            return self.isUgly(n // 5)
        
        # If n is not divisible by 2, 3, or 5, it's not an ugly number
        return False
