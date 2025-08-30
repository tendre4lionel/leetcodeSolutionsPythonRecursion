# 119 Pascal's Triangle II
class Solution(object):
    def getRow(self, rowIndex):
        """
        Recursive solution to get the rowIndex-th row of Pascal's Triangle.

        Approach:
        - Base case: rowIndex == 0 → return [1]
        - Recursively get the previous row
        - Build current row by summing consecutive elements of previous row
        - No loops needed; recursion builds the row
        """

        # Base case: first row
        if rowIndex == 0:
            return [1]

        # Recursively get the previous row
        prev_row = self.getRow(rowIndex - 1)

        # Helper function to recursively build the middle elements
        def build_row(row, index=0):
            if index == len(row) - 1:
                return []  # End of row, no more sums
            return [row[index] + row[index + 1]] + build_row(row, index + 1)

        # Combine first element, recursive middle, last element
        return [1] + build_row(prev_row) + [1]


# ---------------- Example Usage ----------------
sol = Solution()
rowIndex = 4
print(sol.getRow(rowIndex))  # Output: [1, 4, 6, 4, 1]
