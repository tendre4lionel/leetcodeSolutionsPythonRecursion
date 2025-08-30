# 125 Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        """
        Recursive solution to check if a string is a palindrome.

        Approach:
        - Preprocess the string:
            - Convert to lowercase
            - Keep only alphanumeric characters
        - Use two pointers (left and right) recursively:
            - Base case: left >= right → palindrome
            - Compare characters at left and right:
                - If equal → recurse on left+1, right-1
                - If not equal → return False
        """

        # Preprocess string: keep only alphanumeric and lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())

        def helper(left, right):
            # Base case: pointers crossed → palindrome
            if left >= right:
                return True

            # If characters differ → not palindrome
            if s[left] != s[right]:
                return False

            # Recurse inward
            return helper(left + 1, right - 1)

        return helper(0, len(s) - 1)


# ---------------- Example Usage ----------------
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(sol.isPalindrome("race a car"))                      # Output: False
