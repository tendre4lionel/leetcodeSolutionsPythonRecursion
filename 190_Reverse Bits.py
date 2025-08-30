class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Recursive helper with accumulator
        def helper(n, i, acc):
            # Base case: processed 32 bits
            if i == 32:
                return acc

            # Shift accumulator left and add least significant bit of n
            acc = (acc << 1) | (n & 1)

            # Recurse on the remaining bits
            return helper(n >> 1, i + 1, acc)
        
        # Start recursion with index 0 and accumulator 0
        return helper(n, 0, 0)
