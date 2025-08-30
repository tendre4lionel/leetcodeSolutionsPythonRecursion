# 168 Excel Sheet Column Title
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        Recursive solution to convert a column number to an Excel sheet column title.

        Approach:
        - Excel columns are like a 26-based number system but 1-indexed (A=1, B=2, ..., Z=26)
        - Subtract 1 from columnNumber to handle 1-indexing
        - Base case: columnNumber == 0 → return empty string
        - Recursive case:
            1. Compute current character: (columnNumber - 1) % 26 → convert to letter
            2. Recurse on the quotient: (columnNumber - 1) // 26
            3. Combine recursion result + current character
        """

        if columnNumber == 0:
            return ""

        # Compute current character (0-indexed)
        columnNumber -= 1
        current_char = chr(ord('A') + (columnNumber % 26))

        # Recurse on the quotient
        return self.convertToTitle(columnNumber // 26) + current_char


# ---------------- Example Usage ----------------
sol = Solution()
print(sol.convertToTitle(1))    # Output: "A"
print(sol.convertToTitle(28))   # Output: "AB"
print(sol.convertToTitle(701))  # Output: "ZY"
