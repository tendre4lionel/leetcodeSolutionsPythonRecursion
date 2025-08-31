# 415 Add Strings
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        def helper(i, j, carry):
            # Base case: if both strings are fully processed and no carry left
            if i < 0 and j < 0 and carry == 0:
                return ""

            # Get digit from num1
            if i >= 0:
                digit1 = int(num1[i])   # convert char to int
            else:
                digit1 = 0

            # Get digit from num2
            if j >= 0:
                digit2 = int(num2[j])
            else:
                digit2 = 0

            # Sum of digits + carry
            total = digit1 + digit2 + carry
            digit = total % 10
            new_carry = total // 10

            # Recursive call for next digits (move left)
            return helper(i - 1, j - 1, new_carry) + str(digit)

        # Start recursion from last index of each string
        return helper(len(num1) - 1, len(num2) - 1, 0)
