# 191 Number of 1 Bits
class Solution(object):
    def hammingWeight(self, n):
        """
        Calculate the number of '1' bits in the binary representation of n.

        :type n: int
        :rtype: int
        """
        # Start recursion with count = 0
        return self._helper(n, 0)

    def _helper(self, n, count):
        """
        Recursive helper function using tail recursion.

        :param n: Current value of the number, shifting right each step
        :param count: Accumulated number of '1' bits so far
        :return: Total count of '1' bits in the original n
        """

        # Base case: if n is 0, no more bits left to process
        # The accumulated count is the final Hamming weight
        if n == 0:
            return count

        # Extract the least significant bit (LSB) using n & 1
        # This will be 1 if the LSB is 1, otherwise 0
        lsb = n & 1

        # Update the running count by adding the LSB
        new_count = count + lsb

        # Shift n right by 1 to process the next bit in the next recursion
        shifted_n = n >> 1

        # Tail recursion: recursively process the remaining bits
        return self._helper(shifted_n, new_count)
