# 118 Pascal's Triangle
class Solution(object):
    def generate(self, numRows):
        """
        Recursive solution to generate Pascal's Triangle without using loops.

        Approach:
        - Base case: numRows == 1 → return [[1]]
        - Recursively generate triangle up to (numRows - 1)
        - Build new row recursively using a helper function that sums
          consecutive elements from the previous row.
        """

        if numRows == 1:
            return [[1]]

        # Generate triangle up to previous row
        result = self.generate(numRows - 1)
        last_row = result[-1]

        # Helper function to build new row recursively
        def build_row(row, index=0):
            if index == len(row) - 1:
                return [1]  # Last element is always 1
            # Sum current and next element, recurse
            return [row[index] + row[index + 1]] + build_row(row, index + 1)

        # Combine first element, recursive middle, last element
        new_row = [1] + build_row(last_row)
        result.append(new_row)
        return result


# ---------------- Example Usage ----------------
sol = Solution()
numRows = 5
print(sol.generate(numRows))
# Output:
# [
#  [1],
#  [1, 1],
#  [1, 2, 1],
#  [1, 3, 3, 1],
#  [1, 4, 6, 4, 1]
# ]
