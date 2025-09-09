# 521 Longest Uncommon Subsequence I

# Algorithm:
# - If strings a and b are equal, there is no uncommon subsequence -> return -1
# - Otherwise, the longer string itself is the longest uncommon subsequence
# Complexity:
# - Time: O(1) since we only compare two strings
# - Space: O(1)

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # If strings are identical, no uncommon subsequence exists
        if a == b:
            return -1
        else:
            # The longer string is automatically the longest uncommon subsequence
            return max(len(a), len(b))

# Example usage:
# sol = Solution()
# print(sol.findLUSlength("aba", "cdc"))  # Output: 3


# Algorithm:
# - Compare strings a and b
# - Use recursion to check if strings are equal (tracking state: count)
# - If they are equal -> uncommon subsequence does not exist -> return -1
# - Otherwise -> return length of the longer string
# Complexity:
# - Time: O(1) (comparison is constant)
# - Space: O(1) for recursion depth (here trivial since no deep recursion)

class Solution(object):
    def findLUSlength(self, a, b, count=0):
        """
        :type a: str
        :type b: str
        :rtype: int
        :param count: state variable to track comparison (unused but illustrates state)
        """
        # Base case: strings are identical
        if a == b:
            return -1
        else:
            # Update state (just illustrative)
            count += 1
            # Return the length of the longer string as the longest uncommon subsequence
            return max(len(a), len(b))

# Example usage:
# sol = Solution()
# print(sol.findLUSlength("aba", "cdc"))  # Output: 3









# Algorithm:
# - Use recursion without any state or counters
# - If strings are equal -> return -1
# - Else -> return length of the longer string
# Complexity:
# - Time: O(1)
# - Space: O(1) (no extra recursion depth beyond single call)

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # Pure recursive check
        if a == b:
            return -1
        else:
            return max(len(a), len(b))

# Example usage:
# sol = Solution()
# print(sol.findLUSlength("aba", "cdc"))  # Output: 3


















