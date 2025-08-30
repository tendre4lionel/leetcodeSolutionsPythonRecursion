class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        Fully recursive solution: no loops, everything done recursively.
        """

        if not strs:  # Edge case: empty list
            return ""

        def commonPrefixRec(s1, s2, index=0):
            """
            Recursively find the common prefix of two strings starting at index.
            """
            # Base case: if we reach end of either string, stop
            if index >= len(s1) or index >= len(s2):
                return s1[:index]
            # If characters differ, stop
            if s1[index] != s2[index]:
                return s1[:index]
            # Otherwise, continue recursively
            return commonPrefixRec(s1, s2, index + 1)

        def lcpRec(start, end):
            """
            Recursively find LCP in strs[start:end+1].
            """
            # Base case: single string
            if start == end:
                return strs[start]
            # Divide step: split array in two halves
            mid = (start + end) // 2
            leftLCP = lcpRec(start, mid)
            rightLCP = lcpRec(mid + 1, end)
            # Merge step: recursively find common prefix of left and right LCP
            return commonPrefixRec(leftLCP, rightLCP)

        return lcpRec(0, len(strs) - 1)


# -------------------
# Example Runs
# -------------------
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))       # "fl"
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))          # ""
print(solution.longestCommonPrefix(["interview", "internet", "interval"])) # "inte"
print(solution.longestCommonPrefix(["a", "a", "a"]))                     # "a"
