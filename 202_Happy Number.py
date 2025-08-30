# 202 Happy Number
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Recursive function to calculate sum of squares of digits
        def sum_of_squares(num):
            if num == 0:
                return 0
            digit = num % 10
            return digit * digit + sum_of_squares(num // 10)
        
        # Recursive function using Floyd’s cycle detection
        def helper(slow, fast):
            if fast == 1:  # Reached 1 → happy number
                return True
            if slow == fast and slow != 0:  # Cycle detected → not happy
                return False
            # Move slow pointer by one step, fast pointer by two steps
            return helper(sum_of_squares(slow), sum_of_squares(sum_of_squares(fast)))
        
        # Initialize slow and fast pointers
        return helper(n, sum_of_squares(n))
