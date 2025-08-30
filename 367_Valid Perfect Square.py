# 367 Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # Recursive helper function to check if a number is a perfect square
        # We use a binary search approach: check if mid*mid == num
        def check_square(low, high):
            # Base case: if low exceeds high, num is not a perfect square
            if low > high:
                return False
            
            # Find the middle value between low and high
            mid = (low + high) // 2
            
            # Calculate mid squared
            mid_squared = mid * mid
            
            # Check if mid squared equals num
            if mid_squared == num:
                return True  # Found the perfect square
            elif mid_squared < num:
                # If mid squared is smaller, search in the upper half
                return check_square(mid + 1, high)
            else:
                # If mid squared is larger, search in the lower half
                return check_square(low, mid - 1)

        # Start binary search from 1 to num
        return check_square(1, num)

# Example usage
solution = Solution()
print(solution.isPerfectSquare(16))  # True
print(solution.isPerfectSquare(14))  # False
print(solution.isPerfectSquare(1))   # True
