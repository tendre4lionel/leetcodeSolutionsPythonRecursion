# 338 Counting Bits
class Solution(object):
    def countBits(self, n):
        """
        Return an array ans of length n+1 where ans[i] is the number of 1's in the binary representation of i.
        
        :type n: int
        :rtype: List[int]
        """

        # Recursive helper to compute count of 1's for a single number i
        def count_ones(i, memo={}):
            if i == 0:
                return 0
            if i in memo:
                return memo[i]
            # Number of 1's in i = number of 1's in i//2 + last bit of i
            memo[i] = count_ones(i >> 1, memo) + (i & 1)
            return memo[i]

        # Recursive helper to build the answer array from 0 to current index
        def build_array(i):
            if i < 0:
                return []
            # Recursively build array up to i-1
            res = build_array(i - 1)
            # Append the count of 1's for current i
            res.append(count_ones(i))
            return res

        # Build the array from 0 to n
        return build_array(n)


