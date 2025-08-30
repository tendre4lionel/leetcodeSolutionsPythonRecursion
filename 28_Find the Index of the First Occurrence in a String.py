class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        Fully recursive solution to find the first occurrence of needle in haystack.
        Returns the index or -1 if needle is not found.
        """

        # Base case: empty needle always matches at index 0
        if needle == "":
            return 0

        def helper(index):
            """
            Recursively checks if needle occurs starting from haystack[index:].
            
            index: current starting position in haystack
            """
            # If remaining haystack is shorter than needle, can't match
            if index + len(needle) > len(haystack):
                return -1

            # Check if substring starting at index matches needle
            if haystack[index:index+len(needle)] == needle:
                return index  # Found match

            # Recurse to next index
            return helper(index + 1)

        # Start recursion from index 0
        return helper(0)

        # return haystack.find(needle) // ONE LINER



# Example usage:
sol = Solution()
haystack = "hello"
needle = "ll"
print(sol.strStr(haystack, needle))  # Output: 2

haystack = "aaaaa"
needle = "bba"
print(sol.strStr(haystack, needle))  # Output: -1
