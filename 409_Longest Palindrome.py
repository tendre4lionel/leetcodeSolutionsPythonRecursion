# 409 Longest Palindrome
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        length = 0

        for char in s:
            if char in char_set:
                # Found a pair → remove from set and add 2 to length
                char_set.remove(char)
                length += 2
            else:
                # First occurrence → add to set
                char_set.add(char)

        # If any characters remain in set, one can go in the center
        if char_set:
            length += 1

        return length
