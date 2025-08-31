class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Recursive helper function
        def check(i, j):
            """
            i: current index in s
            j: current index in t
            """
            # Base case 1: All characters in s matched
            if i == len(s):
                return True

            # Base case 2: Reached end of t without matching all of s
            if j == len(t):
                return False

            # If current characters match, move both pointers
            if s[i] == t[j]:
                return check(i + 1, j + 1)
            else:
                # Else, move pointer in t to find a match
                return check(i, j + 1)

        # Start recursion from index 0 for both strings
        return check(0, 0)
