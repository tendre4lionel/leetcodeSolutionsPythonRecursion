# 541 Reverse String II
# Algorithm:
# - Iterate over the string in steps of 2k
# - Reverse the first k characters in each 2k block
# - Append the rest as-is
# Complexity:
# - Time: O(n), n = length of string
# - Space: O(n), for building the result string

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = []
        n = len(s)
        
        for i in range(0, n, 2*k):
            # Reverse first k characters
            result.append(s[i:i+k][::-1])
            # Append remaining characters in the 2k block
            result.append(s[i+k:i+2*k])
        
        return ''.join(result)

# Example usage:
# sol = Solution()
# print(sol.reverseStr("abcdefg", 2))  # Output: "bacdfeg"


# Algorithm:
# - Use recursion with current index as state
# - Reverse first k characters starting from index
# - Recursively process the rest of the string
# Complexity:
# - Time: O(n), each character processed once
# - Space: O(n/k) recursion depth

class Solution(object):
    def reverseStr(self, s, k, index=0):
        """
        :type s: str
        :type k: int
        :type index: int, state variable for recursion
        :rtype: str
        """
        # Base case: finished processing string
        if index >= len(s):
            return ''
        
        # Reverse first k characters in this block
        part1 = s[index:index+k][::-1]
        # Keep next k characters as-is
        part2 = s[index+k:index+2*k]
        
        # Recursive call for the rest
        return part1 + part2 + self.reverseStr(s, k, index + 2*k)

# Example usage:
# sol = Solution()
# print(sol.reverseStr("abcdefg", 2))  # Output: "bacdfeg"


# Algorithm:
# - Use slicing to process the string recursively without extra state
# - Reverse first k characters and concatenate with next k unchanged characters
# - Recurse on remaining string
# Complexity:
# - Time: O(n)
# - Space: O(n/k) recursion depth

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s:
            return ''
        return s[:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k)

# Example usage:
# sol = Solution()
# print(sol.reverseStr("abcdefg", 2))  # Output: "bacdfeg"






