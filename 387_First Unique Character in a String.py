# 387 First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """

        # Step 1: Count the frequency of each character
        def count_freq(idx, freq):
            # Base case: reached the end of the string
            if idx == len(s):
                return freq
            char = s[idx]
            freq[char] = freq.get(char, 0) + 1
            return count_freq(idx + 1, freq)

        freq_map = count_freq(0, {})

        # Step 2: Find the first character with frequency 1 recursively
        def find_first(idx):
            # Base case: reached end of string
            if idx == len(s):
                return -1
            if freq_map[s[idx]] == 1:
                return idx
            return find_first(idx + 1)

        return find_first(0)
