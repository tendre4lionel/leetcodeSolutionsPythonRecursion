# 476 Number Complement
class Solution(object):
    def findComplement(self, num):
        """
        Recursively find the complement of an integer using binary string.
        :type num: int
        :rtype: int
        """

        # Convert num to binary string without '0b' prefix
        bin_str = bin(num)[2:]

        # Recursive helper to flip each bit
        def flip_bits(s, index=0):
            # Base case: if we reach the end of the string
            if index == len(s):
                return ""

            # Flip the current bit
            flipped = '0' if s[index] == '1' else '1'

            # Recurse for the rest of the string
            return flipped + flip_bits(s, index + 1)

        # Get the flipped binary string
        flipped_bin = flip_bits(bin_str)

        # Convert back to integer
        return int(flipped_bin, 2)


# Example usage
sol = Solution()
print(sol.findComplement(5))   # 2, because 5 = 101 → complement 010 = 2
print(sol.findComplement(1))   # 0, because 1 = 1 → complement 0 = 0
print(sol.findComplement(10))  # 5, because 10 = 1010 → complement 0101 = 5
