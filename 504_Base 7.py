class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Algorithm (Iterative approach):
        # 1. Handle special case when num == 0 (return "0").
        # 2. Remember if num is negative, and work with absolute value.
        # 3. Repeatedly divide num by 7 and collect remainders.
        # 4. Reverse the collected digits to form base-7.
        # 5. Add "-" back if original num was negative.
        #
        # Time Complexity: O(log_7(n)) 
        # Space Complexity: O(log_7(n))

        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)

        digits = []
        while num > 0:
            digits.append(str(num % 7))  # collect remainder
            num //= 7  # reduce the number

        result = "".join(reversed(digits))

        if negative:
            result = "-" + result

        return result


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Algorithm (Recursive with shared state):
        # 1. Handle 0 explicitly.
        # 2. Use recursion to process quotient first, then remainder.
        # 3. Store digits in a shared list that keeps correct order.
        # 4. Join digits and add "-" if negative.
        #
        # Time Complexity: O(log_7(n)) 
        # Space Complexity: O(log_7(n)) recursion depth + digits list.

        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)

        digits = []

        def helper(n):
            if n == 0:
                return
            helper(n // 7)  # process higher digits first
            digits.append(str(n % 7))

        helper(num)

        result = "".join(digits)
        if negative:
            result = "-" + result
        return result



class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Algorithm (Pure recursion):
        # 1. Handle num == 0 separately.
        # 2. If num < 7, return it directly as string.
        # 3. Otherwise, recursively build quotient result + remainder digit.
        # 4. Add "-" if original number was negative.
        #
        # Time Complexity: O(log_7(n)) 
        # Space Complexity: O(log_7(n)) recursion depth only.

        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)

        def helper(n):
            if n < 7:
                return str(n)
            return helper(n // 7) + str(n % 7)

        result = helper(num)
        if negative:
            result = "-" + result
        return result



