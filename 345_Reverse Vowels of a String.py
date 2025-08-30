class Solution(object):
    def reverseVowels(self, s):
        """
        Reverse only the vowels in a string using recursion.
        :type s: str
        :rtype: str
        """

        # Define the set of vowels (both lowercase and uppercase)
        vowels = set("aeiouAEIOU")

        # Strings in Python are immutable, so convert to a list for in-place modification
        s = list(s)

        def helper(l, r):
            """
            Recursive helper function to swap vowels.
            l = left pointer (start of string moving forward)
            r = right pointer (end of string moving backward)
            """

            # Base case: stop recursion when left pointer crosses or meets right pointer
            if l >= r:
                return

            # Case 1: if the left character is NOT a vowel, just move the left pointer forward
            if s[l] not in vowels:
                helper(l + 1, r)  # recurse with left pointer advanced
                return

            # Case 2: if the right character is NOT a vowel, just move the right pointer backward
            if s[r] not in vowels:
                helper(l, r - 1)  # recurse with right pointer moved left
                return

            # Case 3: if both characters are vowels, swap them
            s[l], s[r] = s[r], s[l]

            # Move both pointers inward after swap, and recurse further
            helper(l + 1, r - 1)

        # Initial recursive call with full string range
        helper(0, len(s) - 1)

        # Convert list back to string and return
        return "".join(s)
