# 461 Hamming Distance
class Solution(object):
    def hammingDistance(self, x, y):
        """
        Calculate the Hamming distance between two integers recursively.
        :type x: int
        :type y: int
        :rtype: int
        """

        # Base case: if both numbers are 0, no bits differ
        if x == 0 and y == 0:
            return 0

        # Check if the least significant bits (LSB) are different
        # x & 1 gives the last bit of x, y & 1 gives the last bit of y
        bit_diff = (x & 1) ^ (y & 1)  # XOR: 1 if different, 0 if same

        # Recursive call: shift both numbers right by 1 to check next bit
        return bit_diff + self.hammingDistance(x >> 1, y >> 1)


# Example usage
sol = Solution()
print(sol.hammingDistance(1, 4))  # 2, because 1 = 001, 4 = 100 in binary
print(sol.hammingDistance(3, 1))  # 1, because 3 = 11, 1 = 01 in binary
print(sol.hammingDistance(7, 15)) # 1, because 7 = 0111, 15 = 1111
