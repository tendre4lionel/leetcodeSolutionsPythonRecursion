# 455 Assign Cookies
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        def helper(i, j):
            # i -> index in g (children), j -> index in s (cookies)
            if i < 0 or j < 0:
                return 0

            if s[j] >= g[i]:
                # assign this cookie to this child
                return 1 + helper(i - 1, j - 1)
            else:
                # cookie too small, skip it
                return helper(i, j - 1)

        return helper(len(g) - 1, len(s) - 1)




"""
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        i = 0  # pointer for children
        j = 0  # pointer for cookies

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:   # cookie satisfies this child
                i += 1         # move to next child
            j += 1             # always move to next cookie

        return i
"""