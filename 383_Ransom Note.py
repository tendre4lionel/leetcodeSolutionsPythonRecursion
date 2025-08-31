# 383 Ransom Note
from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # Create frequency count of magazine letters
        mag_count = Counter(magazine)

        # Recursive helper function
        def helper(idx):
            """
            idx: current index in ransomNote
            """
            # Base case: all characters processed
            if idx == len(ransomNote):
                return True

            char = ransomNote[idx]

            # Check if char is available in magazine
            if mag_count.get(char, 0) > 0:
                # Use one occurrence of the character
                mag_count[char] -= 1

                # Recurse to next character
                result = helper(idx + 1)

                # Backtrack: restore count for other recursion paths
                mag_count[char] += 1

                return result
            else:
                # Character not available
                return False

        # Start recursion from first character
        return helper(0)
