class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        Fully recursive solution to increment a number represented as an array of digits.
        """

        def helper(index):
            """
            Recursively adds 1 to the number starting from the last digit.

            index: current position in digits array (starting from end)
            """
            # Base case: we have moved past the most significant digit
            if index < 0:
                # All digits were 9, so we need an extra digit at the beginning
                digits.insert(0, 1)
                return

            # Add 1 to the current digit if it's the last recursion step
            if digits[index] < 9:
                digits[index] += 1
                return
            else:
                # Current digit is 9 → becomes 0 and carry over 1
                digits[index] = 0
                # Recurse to handle carry in the next more significant digit
                helper(index - 1)

        # Start recursion from the last digit
        helper(len(digits) - 1)
        return digits


# Example usage:
sol = Solution()
print(sol.plusOne([1,2,3]))  # Output: [1,2,4]
print(sol.plusOne([4,3,2,1]))  # Output: [4,3,2,2]
print(sol.plusOne([9,9,9]))    # Output: [1,0,0,0]
