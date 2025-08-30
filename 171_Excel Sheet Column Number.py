# 171 Excel Sheet Column Number
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        Recursive solution to convert an Excel column title to a number.

        Approach:
        - Excel columns are like a 26-based number system (A=1, B=2, ..., Z=26)
        - Base case: empty string → return 0
        - Recursive case:
            1. Convert the last character to a number: ord(columnTitle[-1]) - ord('A') + 1
            2. Recurse on the remaining string: columnTitle[:-1]
            3. Combine: number from recursion * 26 + current digit
        """

        if not columnTitle:
            return 0

        # Last character value
        last_digit = ord(columnTitle[-1]) - ord('A') + 1

        # Recurse on all characters except the last
        return self.titleToNumber(columnTitle[:-1]) * 26 + last_digit


# ---------------- Example Usage ----------------
sol = Solution()
print(sol.titleToNumber("A"))    # Output: 1
print(sol.titleToNumber("AB"))   # Output: 28
print(sol.titleToNumber("ZY"))   # Output: 701
