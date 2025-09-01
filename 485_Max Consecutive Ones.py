# 485 Max Consecutive Ones
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        Fully recursive solution to find the maximum number of consecutive 1's.
        :type nums: List[int]
        :rtype: int
        """

        # Recursive helper function
        def helper(index, current_streak, max_streak):
            """
            :param index: current index in the nums list
            :param current_streak: length of current consecutive 1's streak
            :param max_streak: maximum streak found so far
            """

            # Base case: if we've processed all elements
            if index == len(nums):
                return max_streak

            # If current element is 1, increase streak
            if nums[index] == 1:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                # Reset streak if we hit a 0
                current_streak = 0

            # Recurse on the next index
            return helper(index + 1, current_streak, max_streak)

        # Start recursion from index 0
        return helper(0, 0, 0)


# Example usage
sol = Solution()
print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))  # 3
print(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]))  # 2


"""
Iterative Solution
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        Iterative solution to find the maximum number of consecutive 1's.
        :type nums: List[int]
        :rtype: int
        """

        max_streak = 0      # Longest streak found so far
        current_streak = 0  # Current streak of consecutive 1's

        # Go through each number in the list
        for num in nums:
            if num == 1:
                # Continue the streak
                current_streak += 1
                # Update max streak if needed
                max_streak = max(max_streak, current_streak)
            else:
                # Reset streak when we hit a 0
                current_streak = 0

        return max_streak


# Example usage
sol = Solution()
print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))  # 3
print(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]))  # 2

Key differences:

Recursive:

Passes index, current_streak, and max_streak down the recursion chain.

Base case is when index == len(nums).

Iterative:

Uses a simple for loop.

Updates current_streak and max_streak in-place.

Both run in O(n) time and O(1) extra space (aside from recursion stack in the recursive one).
"""

"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        Pure functional recursion:
        Each call returns (max_streak, current_streak).
        :type nums: List[int]
        :rtype: int
        """

        def helper(index):
            """
            Recursive function that processes nums[index:].
            Returns:
                (max_streak, current_streak)
            """
            # Base case: if we've processed all elements
            if index == len(nums):
                return (0, 0)

            # Recursive call on the rest of the array
            rest_max, rest_current = helper(index + 1)

            if nums[index] == 1:
                # Current streak = 1 + streak of next element
                current_streak = 1 + rest_current
                # Max streak = max(current_streak, rest_max)
                return (max(current_streak, rest_max), current_streak)
            else:
                # Reset streak if current element is 0
                return (rest_max, 0)

        # Extract only the maximum streak from result
        max_streak, _ = helper(0)
        return max_streak


# Example usage
sol = Solution()
print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))  # 3
print(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]))  # 2

"""


