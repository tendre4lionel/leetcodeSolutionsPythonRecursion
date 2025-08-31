# 389 Find the Difference
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        # Recursive helper to count letters in s
        def count_letters(idx, freq):
            # Base case: all characters processed
            if idx == len(s):
                return freq
            char = s[idx]
            freq[char] = freq.get(char, 0) + 1
            return count_letters(idx + 1, freq)

        freq_map = count_letters(0, {})

        # Recursive helper to find extra letter in t
        def find_extra(idx):
            # Base case: reached end of t (safety)
            if idx == len(t):
                return ''
            char = t[idx]
            if freq_map.get(char, 0) > 0:
                # Use one occurrence
                freq_map[char] -= 1
                return find_extra(idx + 1)
            else:
                # This character is the extra one
                return char

        # Start recursion from index 0
        return find_extra(0)


"""
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        # Recursive helper function
        def xor_recursive(idx, result):
            # Base case: reached end of both strings
            if idx == len(t):
                return result

            # XOR character from s if within bounds
            if idx < len(s):
                result ^= ord(s[idx])

            # XOR character from t
            result ^= ord(t[idx])

            # Recurse to next index
            return xor_recursive(idx + 1, result)

        # Start recursion from index 0 with initial result 0
        final_xor = xor_recursive(0, 0)

        # Convert ASCII code to character
        return chr(final_xor)

"""