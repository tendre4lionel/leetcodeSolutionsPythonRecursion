class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        Converts a Roman numeral string into its integer value
        using recursion.
        """

        # Roman numeral to integer mapping
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        def helper(index):
            """
            Recursive function to compute the integer value
            starting from position 'index' in the string.
            """

            # BASE CASE:
            # If index goes beyond the last character, return 0.
            # This stops the recursion.
            if index >= len(s):
                return 0

            # Get the integer value of the current Roman numeral
            current_value = roman[s[index]]

            # STEP 1: Look ahead at the next character (if it exists)
            # If the next Roman numeral has a larger value,
            # then this numeral must be SUBTRACTED (e.g., IV = 4).
            if index + 1 < len(s) and roman[s[index + 1]] > current_value:
                # Subtract current value and move to the next index
                return -current_value + helper(index + 1)
            else:
                # Otherwise, ADD the current value and continue
                return current_value + helper(index + 1)

        # Start recursion at index 0
        return helper(0)


# -------------------
# Example Runs
# -------------------
solution = Solution()
print(solution.romanToInt("III"))     # 3
print(solution.romanToInt("IV"))      # 4
print(solution.romanToInt("IX"))      # 9
print(solution.romanToInt("LVIII"))   # 58
print(solution.romanToInt("MCMXCIV")) # 1994
