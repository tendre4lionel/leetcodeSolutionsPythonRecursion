# 242 Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        """
        Recursively check if t is an anagram of s.
        """

        # Base case: different lengths → not an anagram
        if len(s) != len(t):
            return False

        # Helper function: recursively count characters
        def count_chars(string, index=0, counts=None):
            if counts is None:
                counts = {}
            # Base case: finished string
            if index == len(string):
                return counts
            char = string[index]
            counts[char] = counts.get(char, 0) + 1
            return count_chars(string, index + 1, counts)

        # Count characters for both strings
        count_s = count_chars(s)
        count_t = count_chars(t)

        # Compare the two dictionaries
        return count_s == count_t




"""
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)

"""