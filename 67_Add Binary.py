class Solution(object):
    def addBinary(self, a, b):
        """
        Add two binary strings recursively.
        
        :type a: str
        :type b: str
        :rtype: str
        """

        def helper(i, j, carry):
            """
            Recursive helper function that simulates binary addition 
            starting from the least significant bit (rightmost digit).
            
            i -> current index in string a (starting from the end)
            j -> current index in string b (starting from the end)
            carry -> the carry bit (0 or 1) from the previous addition
            
            Returns:
                A binary string representing the sum of a[:i+1] and b[:j+1]
                plus the carry, in correct order.
            """

            # Base case:
            # If both strings are fully traversed (i < 0, j < 0)
            # and there's no carry left, we are done.
            if i < 0 and j < 0 and carry == 0:
                return ""

            # Get the current digit from string a (if in range), else 0
            x = int(a[i]) if i >= 0 else 0
            # Get the current digit from string b (if in range), else 0
            y = int(b[j]) if j >= 0 else 0

            # Total for this digit = x + y + carry
            total = x + y + carry

            # The resulting binary digit is total % 2 (0 or 1)
            digit = str(total % 2)

            # New carry for the next recursive step = total // 2 (0 or 1)
            new_carry = total // 2

            # Recurse on the remaining digits (moving left in both strings)
            # Build the result from left to right by appending the current digit
            return helper(i - 1, j - 1, new_carry) + digit

        # Start recursion from the last index of both strings with no carry
        return helper(len(a) - 1, len(b) - 1, 0)
