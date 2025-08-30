# 231 Power of Two
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        Determine recursively if a number is a power of two.

        :type n: int
        :rtype: bool
        """

        # Base case 1: 1 is 2^0 → return True
        if n == 1:
            return True

        # Base case 2: n <= 0 or odd numbers (except 1) are not powers of two
        if n <= 0 or n % 2 != 0:
            return False

        # Recursive case: divide n by 2 and check recursively
        return self.isPowerOfTwo(n // 2)


# ---------------- Example Usage ----------------
sol = Solution()
print(sol.isPowerOfTwo(1))   # True, 2^0
print(sol.isPowerOfTwo(16))  # True, 2^4
print(sol.isPowerOfTwo(218)) # False
print(sol.isPowerOfTwo(1024))# True, 2^10
print(sol.isPowerOfTwo(0))   # False
