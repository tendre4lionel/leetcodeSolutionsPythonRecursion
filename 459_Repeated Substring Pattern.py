# 459 Repeated Substring Pattern
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        Fully recursive check if the string can be formed by repeating a substring.
        :type s: str
        :rtype: bool
        """

        # Helper function to check if s appears in t starting at index i
        def is_substring(t, s, i=0):
            # Base case: if remaining length of t is smaller than s, cannot match
            if i + len(s) > len(t):
                return False
            
            # Check if s matches starting at index i
            if t[i:i + len(s)] == s:
                return True
            
            # Recurse to next index
            return is_substring(t, s, i + 1)

        # Create the doubled string minus first and last character
        doubled = s + s
        trimmed = doubled[1:-1]

        # Use recursion to check if original string s appears in trimmed string
        return is_substring(trimmed, s)


# Example usage
sol = Solution()
print(sol.repeatedSubstringPattern("abab"))         # True
print(sol.repeatedSubstringPattern("aba"))          # False
print(sol.repeatedSubstringPattern("abcabcabcabc")) # True


"""
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        Check if s can be formed by repeating a substring.
        :type s: str
        :rtype: bool
        """

        # Trick explanation:
        # 1. Double the string: s + s
        # 2. Remove the first and last character: [1:-1]
        # 3. If original string s appears in this new string,
        #    it must be made by repeating a substring.

        return s in (s + s)[1:-1]

"""

"""
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        Check if the string s can be constructed by repeating a substring.
        :type s: str
        :rtype: bool
        """
        n = len(s)
        
        # Try all possible substring lengths from 1 to half of the string length
        for sub_len in range(1, n // 2 + 1):
            # Only consider lengths that evenly divide the string
            if n % sub_len == 0:
                # Get the substring
                sub = s[:sub_len]
                
                # Repeat the substring enough times to match the original string
                if sub * (n // sub_len) == s:
                    return True  # Found a repeating pattern
        
        # No repeating pattern found
        return False


# Example usage
sol = Solution()
print(sol.repeatedSubstringPattern("abab"))         # True
print(sol.repeatedSubstringPattern("aba"))          # False
print(sol.repeatedSubstringPattern("abcabcabcabc")) # True

"""

"""
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        Check recursively if the string s can be constructed by repeating a substring.
        :type s: str
        :rtype: bool
        """

        # Recursive function to check if the string can be built by repeating
        # a substring of length 'sub_len' starting from index 'start'
        def check_repeat(sub_len, start):
            # Base case: reached the end of the string
            if start == len(s):
                return True
            
            # If current character does not match the corresponding character
            # in the first substring, return False
            if s[start] != s[start % sub_len]:
                return False
            
            # Recurse for the next character
            return check_repeat(sub_len, start + 1)
        
        # Recursive function to try all possible substring lengths starting from 'length'
        def try_lengths(length):
            # If length exceeds half of string, no more possibilities
            if length > len(s) // 2:
                return False
            
            # Only check lengths that evenly divide the string
            if len(s) % length == 0:
                if check_repeat(length, 0):
                    return True
            
            # Try the next possible length
            return try_lengths(length + 1)
        
        # Start recursion from length 1
        return try_lengths(1)


# Example usage
sol = Solution()
print(sol.repeatedSubstringPattern("abab"))         # True
print(sol.repeatedSubstringPattern("aba"))          # False
print(sol.repeatedSubstringPattern("abcabcabcabc")) # True
"""


