class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        Fully recursive solution to find the length of the last word in a string.
        """

        def helper(index):
            """
            Recursively find the length of the last word starting from the end.
            
            index: current index (starting from end of string)
            """
            # Base case: start of string reached
            if index < 0:
                return 0

            # Skip trailing spaces at the end
            if s[index] == ' ':
                return helper(index - 1)

            # Count letters of the last word
            def count_word(i):
                if i < 0 or s[i] == ' ':
                    return 0
                return 1 + count_word(i - 1)

            # Once we hit a non-space, count the word
            return count_word(index)

        # Start recursion from the last index
        return helper(len(s) - 1)


# Example usage:
sol = Solution()
print(sol.lengthOfLastWord("Hello World"))      # Output: 5
print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(sol.lengthOfLastWord("luffy is still joyboy"))        # Output: 6
