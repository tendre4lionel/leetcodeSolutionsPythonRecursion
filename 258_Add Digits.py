# 258 Add Digits: Mathematical Formula Approach (Digital Root)
class Solution(object):
    def addDigits(self, num):
        """
        Return the digital root of the number using modulo operation.
        """
        # If num is 0, we return 0
        if num == 0:
            return 0
        # If num is divisible by 9, the result should be 9
        return 9 if num % 9 == 0 else num % 9


"""
# Iterative Approach
class Solution(object):
    def addDigits(self, num):
        """
        Repeatedly add digits until the result has only one digit.
        """
        # Keep adding digits while num has more than one digit
        while num >= 10:
            num = sum(int(digit) for digit in str(num))  # Sum of digits
        return num

"""

"""
# recursive
class Solution(object):
    def addDigits(self, num):
        """
        Recursively sum digits without using a for loop.
        """
        # Base case: If the number is a single digit, return it
        if num < 10:
            return num
        
        # Recursive case: Sum the digits by extracting the last digit and the rest
        return self.addDigits(num // 10 + num % 10)  # Recurse with the sum of digits



"""