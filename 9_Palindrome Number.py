class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers cannot be palindromes
        if x < 0:
            return False

        s = str(x)  # convert to string

        def helper(left, right):
            # Base case: if pointers cross, it's a palindrome
            if left >= right:
                return True

            # If mismatch found, not a palindrome
            if s[left] != s[right]:
                return False

            # Recurse inward
            return helper(left + 1, right - 1)

        return helper(0, len(s) - 1)


# -------------------
# Example Run
# -------------------
solution = Solution()
print(solution.isPalindrome(121))   # True
print(solution.isPalindrome(-121))  # False
print(solution.isPalindrome(10))    # False
print(solution.isPalindrome(12321)) # True
