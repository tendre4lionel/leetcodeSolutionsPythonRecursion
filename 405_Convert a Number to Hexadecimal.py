# 405 Convert a Number to Hexadecimal
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """

        # Handle zero case
        if num == 0:
            return "0"

        # Handle negative numbers using 32-bit two's complement
        if num < 0:
            num += 2 ** 32  # Convert negative to two's complement

        # Hex characters
        hex_chars = "0123456789abcdef"

        # Recursive helper function
        def convert(n):
            if n == 0:
                return ""
            else:
                return convert(n // 16) + hex_chars[n % 16]

        # Get result and remove leading zeros
        result = convert(num)
        return result.lstrip('0')  # safety, though recursion ensures no leading zeros



solution = Solution()
print(solution.toHex(26))       # Output: "1a"
print(solution.toHex(-1))       # Output: "ffffffff"
print(solution.toHex(0))        # Output: "0"
print(solution.toHex(123456))   # Output: "1e240"
